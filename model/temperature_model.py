import pandas as pd
import streamlit as st


def get_max_temperature_serie():
    pass


def format_value(value):
    if pd.notna(value):  
        return f"{value:.1f}"  #str 1 decimal
    else:  # if NaN
        return ""

def temperature_max_summary_table_model():
    max_summary_df = st.session_state["summary_max_temp_dict"].map(format_value)
    return max_summary_df


def temperature_med_summary_table_model():
    med_summary_df = st.session_state["summary_med_temp_dict"].map(format_value)
    return med_summary_df


def temperature_min_summary_table_model():
    min_summary_df = st.session_state["summary_min_temp_dict"].map(format_value)
    return min_summary_df


def temperature_absolute_records_table_model() -> pd.DataFrame:
    excel_stats_dict = st.session_state["excel_stats_dict"]
    excel_stats_dict["stats_temp"] = excel_stats_dict["stats_temp"].set_index(
        "Estadísticas"
    )
    stats_temp_df = pd.DataFrame(excel_stats_dict["stats_temp"])
    stats_temp_df["Fecha"] = pd.to_datetime(stats_temp_df["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    stats_temp_df["Temperatura [ºC]"] = stats_temp_df["Temperatura [ºC]"].apply(
        lambda x: f"{x:.1f}"
    )
    return stats_temp_df


def temperature_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_temp = pd.DataFrame(
        {
            "Estadísticas": [
                "Media td1 mínima rel. (Rango sel.)",
                "Media td1 máxima rel. (Rango sel.)",
                "Mínima rel. (Rango sel.)",
                "Mínima Max. rel. (Rango sel.)",
                "Máxima rel. (Rango sel.)",
                "Máxima Min. rel. (Rango sel.)",
                "Min. amplitud rel. (Rango sel.)",
                "Max. amplitud rel. (Rango sel.)",
            ],
            "Fecha": pd.to_datetime([0, 0, 0, 0, 0, 0, 0, 0]),
            "Temperatura [ºC]": [0., 0., 0., 0., 0., 0., 0., 0.],
        }
    )

    df_stats_rel_temp = df_stats_rel_temp.set_index("Estadísticas")

    df_stats_rel_temp.loc["Media td1 mínima rel. (Rango sel.)", "Temperatura [ºC]"] = (
        df["T. med1."].min()
    )
    df_stats_rel_temp.loc["Media td1 mínima rel. (Rango sel.)", "Fecha"] = df[
        "T. med1."
    ].idxmin()
    df_stats_rel_temp.loc["Media td1 máxima rel. (Rango sel.)", "Temperatura [ºC]"] = (
        df["T. med1."].max()
    )
    df_stats_rel_temp.loc["Media td1 máxima rel. (Rango sel.)", "Fecha"] = df[
        "T. med1."
    ].idxmax()
    df_stats_rel_temp.loc["Mínima rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Min."
    ].min()
    df_stats_rel_temp.loc["Mínima rel. (Rango sel.)", "Fecha"] = df["T. Min."].idxmin()
    df_stats_rel_temp.loc["Mínima Max. rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Min."
    ].max()
    df_stats_rel_temp.loc["Mínima Max. rel. (Rango sel.)", "Fecha"] = df[
        "T. Min."
    ].idxmax()
    df_stats_rel_temp.loc["Máxima rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Max."
    ].max()
    df_stats_rel_temp.loc["Máxima rel. (Rango sel.)", "Fecha"] = df["T. Max."].idxmax()
    df_stats_rel_temp.loc["Máxima Min. rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Max."
    ].min()
    df_stats_rel_temp.loc["Máxima Min. rel. (Rango sel.)", "Fecha"] = df[
        "T. Max."
    ].idxmin()
    df_stats_rel_temp.loc["Min. amplitud rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Amp."
    ].min()
    df_stats_rel_temp.loc["Min. amplitud rel. (Rango sel.)", "Fecha"] = df[
        "T. Amp."
    ].idxmin()
    df_stats_rel_temp.loc["Max. amplitud rel. (Rango sel.)", "Temperatura [ºC]"] = df[
        "T. Amp."
    ].max()
    df_stats_rel_temp.loc["Max. amplitud rel. (Rango sel.)", "Fecha"] = df[
        "T. Amp."
    ].idxmax()

    df_stats_rel_temp["Fecha"] = pd.to_datetime(df_stats_rel_temp["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    df_stats_rel_temp["Temperatura [ºC]"] = df_stats_rel_temp["Temperatura [ºC]"].apply(
        lambda x: f"{x:.1f}"
    )

    return df_stats_rel_temp
