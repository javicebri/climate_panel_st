import pandas as pd
import streamlit as st


def get_max_humidity_serie():
    pass


def format_value(value):
    if isinstance(value, str):
        return value
    elif isinstance(value, int):
        return str(value)
    elif pd.notna(value):
        return f"{value:.1f}"  # str 1 decimal
    else:  # if NaN
        return ""


def humidity_max_summary_table_model():
    max_summary_df = st.session_state["summary_max_hum_dict"].map(format_value)
    max_summary_df.index = max_summary_df.index.map(format_value)
    return max_summary_df


def humidity_min_summary_table_model():
    min_summary_df = st.session_state["summary_min_hum_dict"].map(format_value)
    min_summary_df.index = min_summary_df.index.map(format_value)
    return min_summary_df


def humidity_absolute_records_table_model() -> pd.DataFrame:
    excel_stats_dict = st.session_state["excel_stats_dict"]
    excel_stats_dict["stats_hum"] = excel_stats_dict["stats_hum"].set_index(
        "Estadísticas"
    )
    stats_hum_df = pd.DataFrame(excel_stats_dict["stats_hum"])
    stats_hum_df["Fecha"] = pd.to_datetime(stats_hum_df["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    stats_hum_df["Humedad [%]"] = stats_hum_df["Humedad [%]"].apply(
        lambda x: f"{x:.1f}"
    )
    return stats_hum_df


def humidity_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_hum = pd.DataFrame(
        {
            "Estadísticas": [
                "Mínima rel. (Rango sel.)",
                "Mínima Max. rel. (Rango sel.)",
                "Máxima rel. (Rango sel.)",
                "Máxima Min. rel. (Rango sel.)",
            ],
            "Fecha": pd.to_datetime([0, 0, 0, 0]),
            "Humedad [%]": [0.0, 0.0, 0.0, 0.0],
        }
    )

    df_stats_rel_hum = df_stats_rel_hum.set_index("Estadísticas")

    df_stats_rel_hum.loc["Mínima rel. (Rango sel.)", "Humedad [%]"] = df[
        "P. Min."
    ].min()
    df_stats_rel_hum.loc["Mínima rel. (Rango sel.)", "Fecha"] = df["P. Min."].idxmin()
    df_stats_rel_hum.loc["Mínima Max. rel. (Rango sel.)", "Humedad [%]"] = df[
        "P. Min."
    ].max()
    df_stats_rel_hum.loc["Mínima Max. rel. (Rango sel.)", "Fecha"] = df[
        "P. Min."
    ].idxmax()
    df_stats_rel_hum.loc["Máxima rel. (Rango sel.)", "Humedad [%]"] = df[
        "P. Max."
    ].max()
    df_stats_rel_hum.loc["Máxima rel. (Rango sel.)", "Fecha"] = df["P. Max."].idxmax()
    df_stats_rel_hum.loc["Máxima Min. rel. (Rango sel.)", "Humedad [%]"] = df[
        "P. Max."
    ].min()
    df_stats_rel_hum.loc["Máxima Min. rel. (Rango sel.)", "Fecha"] = df[
        "P. Max."
    ].idxmin()


    df_stats_rel_hum["Fecha"] = pd.to_datetime(df_stats_rel_hum["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    df_stats_rel_hum["Humedad [%]"] = df_stats_rel_hum["Humedad [%]"].apply(
        lambda x: f"{x:.1f}"
    )

    return df_stats_rel_hum
