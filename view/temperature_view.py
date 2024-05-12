import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from assets.texts import texts

from controller.temperature_controller import (
    temperature_relative_records_table_controller,
    temperature_absolute_records_table_controller,
    temperature_max_summary_table_controller,
    temperature_med_summary_table_controller,
    temperature_min_summary_table_controller,
    temperature_heatmap_max_controller,
    temperature_heatmap_min_controller,
    temperature_trend_max_controller,
    temperature_trend_min_controller,
)


def show():
    init_date = pd.to_datetime(st.session_state["init_date"])
    last_date = pd.to_datetime(st.session_state["last_date"])

    df = st.session_state["df_out"].copy()
    filtdred_df = df[(df.index >= init_date) & (df.index <= last_date)]
    max_min_temperature_plot(df=filtdred_df)
    med_temperature_plot(df=filtdred_df)
    amp_temperature_plot(df=filtdred_df)
    temperature_relative_records_table(df=filtdred_df)
    temperature_absolute_records_table()
    temperature_max_summary_table()
    temperature_min_summary_table()
    temperature_med_summary_table()
    temperature_heatmap_max()
    temperature_heatmap_min()
    temperature_trend_max()
    temperature_trend_min()


@st.cache_data()
def temperature_trend_min():
    df = temperature_trend_min_controller()
    t_min_values = df["T. Min."].tolist()
    t_trend_values = df["Regresión T. Min."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_trend_values,
            mode="lines",
            name="Tendencia.",
            line=dict(color="#2222ff"),
        )
    )

    # fig.add_trace(
    #     go.Scatter(
    #         x=df.index,
    #         y=t_min_values,
    #         mode="lines",
    #         name="T. Min.",
    #         line=dict(color="#6666ff"),
    #     )
    # )

    fig.update_layout(
        title=texts.min_trend_temperature_plot_title,
        xaxis_title=texts.min_trend_temperature_trend_plot_xaxis_title,
        yaxis_title=texts.min_temperature_trend_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)


@st.cache_data()
def temperature_trend_max():
    df = temperature_trend_max_controller()
    # t_max_values = df['T. Max.'].tolist()
    t_trend_values = df["Regresión T. Max."].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=t_trend_values,
            mode="lines",
            name="Tendencia",
            line=dict(color="#ff2222"),
        )
    )

    # fig.add_trace(
    #     go.Scatter(
    #         x=df.index,
    #         y=t_max_values,
    #         mode="lines",
    #         name="T. Max.",
    #         line=dict(color="#ff6666"),
    #     )
    # )

    fig.update_layout(
        title=texts.max_trend_temperature_plot_title,
        xaxis_title=texts.max_trend_temperature_trend_plot_xaxis_title,
        yaxis_title=texts.max_temperature_trend_plot_yaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    st.plotly_chart(fig)


@st.cache_data()
def temperature_heatmap_max():
    st.write(texts.max_heatmap)
    df_heatmap_max = temperature_heatmap_max_controller()

    fig = px.imshow(
        df_heatmap_max, text_auto=True, aspect="auto", color_continuous_scale="reds"
    )
    # fig.update_yaxes(tickmode='array', tickvals=list(range(len(df.index))), ticktext=list(df.index))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


@st.cache_data()
def temperature_heatmap_min():
    st.write(texts.min_heatmap)
    df_heatmap_min = temperature_heatmap_min_controller()

    fig = px.imshow(
        df_heatmap_min,
        text_auto=True,
        aspect="auto",
        color_continuous_scale=px.colors.sequential.Blues[::-1],
    )
    # fig.update_yaxes(tickmode='array', tickvals=list(range(len(df.index))), ticktext=list(df.index))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


def temperature_max_summary_table():
    max_summary_df = temperature_max_summary_table_controller()
    st.write(texts.max_summary)
    st.table(max_summary_df)


def temperature_med_summary_table():
    med_summary_df = temperature_med_summary_table_controller()
    st.write(texts.med_summary)
    st.table(med_summary_df)


def temperature_min_summary_table():
    min_summary_df = temperature_min_summary_table_controller()
    st.write(texts.min_summary)
    st.table(min_summary_df)


def temperature_absolute_records_table():
    # Get absolute records df
    stats_abs_temp_df = temperature_absolute_records_table_controller()
    st.write(texts.temperature_absolute_records)
    st.table(stats_abs_temp_df)


def temperature_relative_records_table(df: pd.DataFrame):
    # Get relative records df
    df_stats_rel_temp = temperature_relative_records_table_controller(df)
    st.write(texts.temperature_relative_records)
    st.table(df_stats_rel_temp)


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
