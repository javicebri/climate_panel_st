import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from assets.texts import texts

from controller.pressure_controller import (
    pressure_relative_records_table_controller,
    pressure_absolute_records_table_controller,
    pressure_max_summary_table_controller,
    pressure_min_summary_table_controller,
)


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    max_min_pressure_plot(df=filtdred_df)
    pressure_relative_records_table(df=filtdred_df)
    pressure_absolute_records_table()
    pressure_max_summary_table()
    pressure_min_summary_table()


def pressure_max_summary_table():
    max_summary_df = pressure_max_summary_table_controller()
    st.write(texts.pressure_max_summary)
    st.table(max_summary_df)


def pressure_min_summary_table():
    min_summary_df = pressure_min_summary_table_controller()
    st.write(texts.pressure_min_summary)
    st.table(min_summary_df)


def pressure_absolute_records_table():
    # Get absolute records df
    stats_abs_temp_df = pressure_absolute_records_table_controller()
    st.write(texts.pressure_absolute_records)
    st.table(stats_abs_temp_df)


def pressure_relative_records_table(df: pd.DataFrame):
    # Get relative records df
    df_stats_rel_temp = pressure_relative_records_table_controller(df)
    st.write(texts.pressure_relative_records)
    st.table(df_stats_rel_temp)


@st.cache_data()
def max_min_pressure_plot(df: pd.DataFrame):
    t_min_values = df["T. Min."].tolist()
    t_max_values = df["T. Max."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_min_values,
            mode="lines",
            name="T. Min.",
            line=dict(color="#2222ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_max_values,
            mode="lines",
            name="T. Max.",
            line=dict(color="#ff2222"),
        )
    )

    fig.update_layout(
        title=texts.max_min_pressure_plot_title,
        xaxis_title=texts.max_min_pressure_plot_xaxis_title,
        yaxis_title=texts.max_min_pressure_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)
