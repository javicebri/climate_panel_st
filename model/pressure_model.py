import pandas as pd
import streamlit as st


def get_max_pressure_serie():
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


def pressure_max_summary_table_model():
    max_summary_df = st.session_state["summary_max_press_dict"].map(format_value)
    max_summary_df.index = max_summary_df.index.map(format_value)
    return max_summary_df


def pressure_min_summary_table_model():
    min_summary_df = st.session_state["summary_min_press_dict"].map(format_value)
    min_summary_df.index = min_summary_df.index.map(format_value)
    return min_summary_df


def pressure_absolute_records_table_model() -> pd.DataFrame:
    excel_stats_dict = st.session_state["excel_stats_dict"]
    excel_stats_dict["stats_press"] = excel_stats_dict["stats_press"].set_index(
        "Estadísticas"
    )
    stats_press_df = pd.DataFrame(excel_stats_dict["stats_press"])
    stats_press_df["Fecha"] = pd.to_datetime(stats_press_df["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    stats_press_df["Presión [hPa]"] = stats_press_df["Presión [hPa]"].apply(
        lambda x: f"{x:.1f}"
    )
    return stats_press_df


def pressure_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_press = pd.DataFrame(
        {
            "Estadísticas": [
                "Mínima rel. (Rango sel.)",
                "Mínima Max. rel. (Rango sel.)",
                "Máxima rel. (Rango sel.)",
                "Máxima Min. rel. (Rango sel.)",
            ],
            "Fecha": pd.to_datetime([0, 0, 0, 0]),
            "Presión [hPa]": [0.0, 0.0, 0.0, 0.0],
        }
    )

    df_stats_rel_press = df_stats_rel_press.set_index("Estadísticas")

    df_stats_rel_press.loc["Mínima rel. (Rango sel.)", "Presión [hPa]"] = df[
        "P. Min."
    ].min()
    df_stats_rel_press.loc["Mínima rel. (Rango sel.)", "Fecha"] = df["P. Min."].idxmin()
    df_stats_rel_press.loc["Mínima Max. rel. (Rango sel.)", "Presión [hPa]"] = df[
        "P. Min."
    ].max()
    df_stats_rel_press.loc["Mínima Max. rel. (Rango sel.)", "Fecha"] = df[
        "P. Min."
    ].idxmax()
    df_stats_rel_press.loc["Máxima rel. (Rango sel.)", "Presión [hPa]"] = df[
        "P. Max."
    ].max()
    df_stats_rel_press.loc["Máxima rel. (Rango sel.)", "Fecha"] = df["P. Max."].idxmax()
    df_stats_rel_press.loc["Máxima Min. rel. (Rango sel.)", "Presión [hPa]"] = df[
        "P. Max."
    ].min()
    df_stats_rel_press.loc["Máxima Min. rel. (Rango sel.)", "Fecha"] = df[
        "P. Max."
    ].idxmin()


    df_stats_rel_press["Fecha"] = pd.to_datetime(df_stats_rel_press["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    df_stats_rel_press["Presión [hPa]"] = df_stats_rel_press["Presión [hPa]"].apply(
        lambda x: f"{x:.1f}"
    )

    return df_stats_rel_press
