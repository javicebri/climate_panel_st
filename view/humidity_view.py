import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from assets.texts import texts

from controller.humidity_controller import (
    humidity_relative_records_table_controller,
    humidity_absolute_records_table_controller,
    humidity_max_summary_table_controller,
    humidity_min_summary_table_controller,
)


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    max_min_humidity_plot(df=filtdred_df)
    humidity_relative_records_table(df=filtdred_df)
    humidity_absolute_records_table()
    humidity_max_summary_table()
    humidity_min_summary_table()


def humidity_max_summary_table():
    max_summary_df = humidity_max_summary_table_controller()
    st.write(texts.humidity_max_summary)
    st.table(max_summary_df)


def humidity_min_summary_table():
    min_summary_df = humidity_min_summary_table_controller()
    st.write(texts.humidity_min_summary)
    st.table(min_summary_df)


def humidity_absolute_records_table():
    # Get absolute records df
    stats_abs_temp_df = humidity_absolute_records_table_controller()
    st.write(texts.humidity_absolute_records)
    st.table(stats_abs_temp_df)


def humidity_relative_records_table(df: pd.DataFrame):
    # Get relative records df
    df_stats_rel_temp = humidity_relative_records_table_controller(df)
    st.write(texts.humidity_relative_records)
    st.table(df_stats_rel_temp)


@st.cache_data()
def max_min_humidity_plot(df: pd.DataFrame):
    t_min_values = df["H. Min."].tolist()
    t_max_values = df["H. Max."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_min_values,
            mode="lines",
            name="H. Min.",
            line=dict(color="#2222ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_max_values,
            mode="lines",
            name="H. Max.",
            line=dict(color="#ff2222"),
        )
    )

    fig.update_layout(
        title=texts.max_min_humidity_plot_title,
        xaxis_title=texts.max_min_humidity_plot_xaxis_title,
        yaxis_title=texts.max_min_humidity_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)
