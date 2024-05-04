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

    df_input_res = pd.read_csv(input_res_path, sep=";", index_col=[0])

    excel_compare_dict = pd.read_excel(
        input_compare_path, sheet_name=None, index_col=None
    )

    excel_predict_dict = pd.read_excel(
        input_predict_path, sheet_name=None, index_col=None
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

    st.session_state["df_out"] = df_out
    st.session_state["df_input_trend"] = df_input_trend
    st.session_state["df_input_res"] = df_input_res
    st.session_state["excel_compare_dict"] = excel_compare_dict
    st.session_state["excel_predict_dict"] = excel_predict_dict
    st.session_state["unit_dict"] = unit_dict
