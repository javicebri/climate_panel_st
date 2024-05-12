import os
import pandas as pd
import streamlit as st
from global_vars import data_path


def load_data_session():
    """
    Load dataframes in session state (as global variables)
    """

    input_name = "ESCLM1900000019184A.csv"
    input_trend_name = "ESCLM1900000019184A_trend.csv"
    input_res_name = "ESCLM1900000019184A_res.csv"
    input_stats_name = "ESCLM1900000019184A_stats.xlsx"
    input_compare_name = "ESCLM1900000019184A_compare.xlsx"
    input_predict_name = "ESCLM1900000019184A_predict.xlsx"

    input_path = os.path.join(data_path, input_name)
    input_trend_path = os.path.join(data_path, input_trend_name)
    input_res_path = os.path.join(data_path, input_res_name)
    input_stats_path = os.path.join(data_path, input_stats_name)
    input_compare_path = os.path.join(data_path, input_compare_name)
    input_predict_path = os.path.join(data_path, input_predict_name)

    df_input = pd.read_csv(input_path, sep=";", index_col=[0])
    df_input.index = pd.to_datetime(df_input.index)
    df_out = df_input.copy()

    df_input_trend = pd.read_csv(input_trend_path, sep=";", index_col=[0])
    df_input_trend.index = pd.to_datetime(df_input_trend.index)

    excel_stats_dict = pd.read_excel(input_stats_path, sheet_name=None, index_col=None)

    df_input_res = pd.read_csv(input_res_path, sep=";", index_col=[0])

    excel_compare_dict = pd.read_excel(
        input_compare_path, sheet_name=None, index_col=None
    )

    excel_predict_dict = pd.read_excel(
        input_predict_path, sheet_name=None, index_col=None
    )

    summary_max_temp_df = pd.read_excel(
        input_stats_path, sheet_name="T. Max. mes", index_col=[0]
    )
    summary_med_temp_df = pd.read_excel(
        input_stats_path, sheet_name="T. med1. mes", index_col=[0]
    )
    summary_min_temp_df = pd.read_excel(
        input_stats_path, sheet_name="T. Min. mes", index_col=[0]
    )

    summary_max_press_df = pd.read_excel(
        input_stats_path, sheet_name="P. Max. mes", index_col=[0]
    )
    summary_min_press_df = pd.read_excel(
        input_stats_path, sheet_name="P. Min. mes", index_col=[0]
    )

    summary_max_hum_df = pd.read_excel(
        input_stats_path, sheet_name="H. Max. mes", index_col=[0]
    )
    summary_min_hum_df = pd.read_excel(
        input_stats_path, sheet_name="H. Min. mes", index_col=[0]
    )

    summary_max_wind_df = pd.read_excel(
        input_stats_path, sheet_name="Vel. mes", index_col=[0]
    )

    summary_precipitation_df = pd.read_excel(
        input_stats_path, sheet_name="Precipitación mes", index_col=[0]
    )

    unit_dict = {
        "T. Max.": "[ºC]",
        "T. Min.": "[ºC]",
        "H. Max.": "[%]",
        "H. Min.": "[%]",
        "P. Max.": "[hPa]",
        "P. Min.": "[hPa]",
        "Vel.": "[Km/h]",
        "Precipitación": "[l/m2]",
    }

    st.session_state = {}

    st.session_state["df_out"] = df_out
    st.session_state["df_input_trend"] = df_input_trend
    st.session_state["df_input_res"] = df_input_res
    st.session_state["excel_stats_dict"] = excel_stats_dict
    st.session_state["excel_compare_dict"] = excel_compare_dict
    st.session_state["excel_predict_dict"] = excel_predict_dict
    st.session_state["summary_max_temp_dict"] = summary_max_temp_df
    st.session_state["summary_med_temp_dict"] = summary_med_temp_df
    st.session_state["summary_min_temp_dict"] = summary_min_temp_df
    st.session_state["summary_max_press_dict"] = summary_max_press_df
    st.session_state["summary_min_press_dict"] = summary_min_press_df
    st.session_state["summary_max_hum_dict"] = summary_max_hum_df
    st.session_state["summary_min_hum_dict"] = summary_min_hum_df
    st.session_state["summary_max_wind_dict"] = summary_max_wind_df
    st.session_state["summary_precipitation_dict"] = summary_precipitation_df

    st.session_state["unit_dict"] = unit_dict
