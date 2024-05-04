import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from assets.texts import texts

from controller.temperature_controller import max_temperature_controller


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    max_min_temperature_plot(df=filtdred_df)
    med_temperature_plot(df=filtdred_df)
    amp_temperature_plot(df=filtdred_df)

@st.cache_data()
def max_min_temperature_plot(df: pd.DataFrame):
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
        title=texts.max_min_temperature_plot_title,
        xaxis_title=texts.max_min_temperature_plot_xaxis_title,
        yaxis_title=texts.max_min_temperature_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)

@st.cache_data()
def med_temperature_plot(df: pd.DataFrame):
    """ """
    t_med_values = df["T. med1."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_med_values,
            mode="lines",
            name="T. med1.",
            line=dict(color="#ffaa00"),
        )
    )

    fig.update_layout(
        title=texts.med_temperature_plot_title,
        xaxis_title=texts.med_temperature_plot_xaxis_title,
        yaxis_title=texts.med_temperature_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)

@st.cache_data()
def amp_temperature_plot(df: pd.DataFrame):
    """ """
    t_med_values = df["T. Amp."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_med_values,
            mode="lines",
            name="T. med1.",
            line=dict(dict(color="#ff7755")),
        )
    )

    fig.update_layout(
        title=texts.amp_temperature_plot_title,
        xaxis_title=texts.amp_temperature_plot_xaxis_title,
        yaxis_title=texts.amp_temperature_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)
