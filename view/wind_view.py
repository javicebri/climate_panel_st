import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from assets.texts import texts

from controller.wind_controller import (
    wind_relative_records_table_controller,
    wind_absolute_records_table_controller,
    wind_max_summary_table_controller,
    wind_heatmap_max_controller
)


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    max_wind_plot(df=filtdred_df)
    wind_relative_records_table(df=filtdred_df)
    wind_absolute_records_table()
    wind_max_summary_table()
    wind_heatmap_max()

@st.cache_data()
def wind_heatmap_max():
    st.write(texts.wind_max_heatmap)
    df_heatmap_max = wind_heatmap_max_controller()

    fig = px.imshow(
        df_heatmap_max, text_auto=True, aspect="auto", color_continuous_scale="blues"
    )
    # fig.update_yaxes(tickmode='array', tickvals=list(range(len(df.index))), ticktext=list(df.index))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


def wind_max_summary_table():
    max_summary_df = wind_max_summary_table_controller()
    st.write(texts.wind_max_summary)
    st.table(max_summary_df)


def wind_absolute_records_table():
    # Get absolute records df
    stats_abs_temp_df = wind_absolute_records_table_controller()
    st.write(texts.wind_absolute_records)
    st.table(stats_abs_temp_df)


def wind_relative_records_table(df: pd.DataFrame):
    # Get relative records df
    df_stats_rel_temp = wind_relative_records_table_controller(df)
    st.write(texts.wind_relative_records)
    st.table(df_stats_rel_temp)


@st.cache_data()
def max_wind_plot(df: pd.DataFrame):
    t_max_values = df["Vel."].tolist()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_max_values,
            mode="lines",
            name="Vel.",
            line=dict(color="#2222ff"),
        )
    )

    fig.update_layout(
        title=texts.max_wind_plot_title,
        xaxis_title=texts.max_wind_plot_xaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)
