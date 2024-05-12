import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from assets.texts import texts

from controller.precipitation_controller import (
    precipitation_relative_records_table_controller,
    precipitation_absolute_records_table_controller,
    precipitation_summary_table_controller,
    precipitation_heatmap_controller
)


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    precipitation_plot(df=filtdred_df)
    precipitation_relative_records_table(df=filtdred_df)
    precipitation_absolute_records_table()
    precipitation_summary_table()
    precipitation_heatmap()

@st.cache_data()
def precipitation_heatmap():
    st.write(texts.precipitation_heatmap)
    df_heatmap = precipitation_heatmap_controller()

    fig = px.imshow(
        df_heatmap, text_auto=True, aspect="auto", color_continuous_scale="blues"
    )
    # fig.update_yaxes(tickmode='array', tickvals=list(range(len(df.index))), ticktext=list(df.index))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


def precipitation_summary_table():
    summary_df = precipitation_summary_table_controller()
    st.write(texts.precipitation_summary)
    st.table(summary_df)


def precipitation_absolute_records_table():
    # Get absolute records df
    stats_abs_temp_df = precipitation_absolute_records_table_controller()
    st.write(texts.precipitation_absolute_records)
    st.table(stats_abs_temp_df)


def precipitation_relative_records_table(df: pd.DataFrame):
    # Get relative records df
    df_stats_rel_temp = precipitation_relative_records_table_controller(df)
    st.write(texts.precipitation_relative_records)
    st.table(df_stats_rel_temp)


@st.cache_data()
def precipitation_plot(df: pd.DataFrame):
    precipitation_values = df["Precipitación"].tolist()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=precipitation_values,
            mode="lines",
            name="Precipitación",
            line=dict(color="#2222ff"),
        )
    )

    fig.update_layout(
        title=texts.precipitation_plot_title,
        xaxis_title=texts.precipitation_plot_xaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)
