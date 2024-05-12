import pandas as pd
import streamlit as st
import numpy as np


def get_precipitation_serie():
    pass


def format_value(value):
    if isinstance(value, str):
        if value == "-":
            value = ""
        return value
    elif isinstance(value, int):
        return str(value)
    elif pd.notna(value):
        return f"{value:.1f}"  # str 1 decimal
    else:  # if NaN
        return ""


def precipitation_summary_table_model():
    summary_df = st.session_state["summary_precipitation_dict"].map(format_value)
    summary_df.index = summary_df.index.map(format_value)
    return summary_df


def precipitation_absolute_records_table_model() -> pd.DataFrame:
    excel_stats_dict = st.session_state["excel_stats_dict"]
    excel_stats_dict["stats_prec"] = excel_stats_dict["stats_prec"].set_index(
        "Estadísticas"
    )
    stats_prec_df = pd.DataFrame(excel_stats_dict["stats_prec"])
    stats_prec_df["Fecha"] = pd.to_datetime(stats_prec_df["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )

    stats_prec_df["Precipitación [l/m2]"] = stats_prec_df["Precipitación [l/m2]"].apply(
        format_value
    )
    stats_prec_df["Días"] = stats_prec_df["Días"].apply(format_value)

    return stats_prec_df


def precipitation_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_precipitation = pd.DataFrame(
        {
            "Estadísticas": [
                "Máxima acumulada en un día rel. (Rango sel.)",
                "Máx. días seguidos de precipitación rel. (Rango sel.)",
                "Máx. días seguidos de sequía rel. (Rango sel.)",
            ],
            "Fecha": pd.to_datetime([0, 0, 0]),
            "Precipitación [l/m2]": [0.0, "-", "-"],
            "Días": ["-", 0, 0],
        }
    )

    df_stats_rel_precipitation = df_stats_rel_precipitation.set_index("Estadísticas")

    df["Prec. Acumulado"] = np.zeros([df.shape[0], 1])
    rain_position = df.columns.get_loc("Precipitación")
    arain_position = df.columns.get_loc("Prec. Acumulado")
    for i in range(df.shape[0]):
        if df.iloc[i, rain_position] != 0:
            df.iloc[i, arain_position] = 1
            pass
    df["Cuenta_lluvia"] = (
        df["Prec. Acumulado"].groupby((df["Prec. Acumulado"] == 0).cumsum()).cumcount()
    )
    df["Cuenta_sequía"] = (
        df["Prec. Acumulado"].groupby((df["Prec. Acumulado"] != 0).cumsum()).cumcount()
    )
    df_stats_rel_precipitation.loc[
        "Máx. días seguidos de precipitación rel. (Rango sel.)", "Días"
    ] = df["Cuenta_lluvia"].max()
    df_stats_rel_precipitation.loc[
        "Máx. días seguidos de precipitación rel. (Rango sel.)", "Fecha"
    ] = df["Cuenta_lluvia"].idxmax()
    df_stats_rel_precipitation.loc[
        "Máx. días seguidos de sequía rel. (Rango sel.)", "Días"
    ] = df["Cuenta_sequía"].max()
    df_stats_rel_precipitation.loc[
        "Máx. días seguidos de sequía rel. (Rango sel.)", "Fecha"
    ] = df["Cuenta_sequía"].idxmax()

    df_stats_rel_precipitation.loc[
        "Máxima acumulada en un día rel. (Rango sel.)", "Precipitación [l/m2]"
    ] = df["Precipitación"].max()
    df_stats_rel_precipitation.loc[
        "Máxima acumulada en un día rel. (Rango sel.)", "Fecha"
    ] = df["Precipitación"].idxmax()

    df_stats_rel_precipitation["Fecha"] = pd.to_datetime(
        df_stats_rel_precipitation["Fecha"]
    ).dt.strftime("%d-%m-%Y")
    df_stats_rel_precipitation["Precipitación [l/m2]"] = df_stats_rel_precipitation[
        "Precipitación [l/m2]"
    ].apply(format_value)
    df_stats_rel_precipitation["Días"] = df_stats_rel_precipitation["Días"].apply(
        format_value
    )

    return df_stats_rel_precipitation


def precipitation_heatmap_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop("Interanual")
    df = df.drop("Anual", axis=1)
    return df
