import pandas as pd
import streamlit as st


def get_max_wind_serie():
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


def wind_max_summary_table_model():
    max_summary_df = st.session_state["summary_max_wind_dict"].map(format_value)
    max_summary_df.index = max_summary_df.index.map(format_value)
    return max_summary_df


def wind_absolute_records_table_model() -> pd.DataFrame:
    excel_stats_dict = st.session_state["excel_stats_dict"]
    excel_stats_dict["stats_wind"] = excel_stats_dict["stats_wind"].set_index(
        "Estadísticas"
    )
    stats_wind_df = pd.DataFrame(excel_stats_dict["stats_wind"])
    stats_wind_df["Fecha"] = pd.to_datetime(stats_wind_df["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    stats_wind_df["Velocidad [Km/h]"] = stats_wind_df["Velocidad [Km/h]"].apply(
        lambda x: f"{x:.1f}"
    )
    return stats_wind_df


def wind_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_wind = pd.DataFrame(
        {
            "Estadísticas": [
                "Máxima rel. (Rango sel.)",
                "Máxima Min. rel. (Rango sel.)",
            ],
            "Fecha": pd.to_datetime([0, 0]),
            "Velocidad [Km/h]": [0.0, 0.0 ],
        }
    )

    df_stats_rel_wind = df_stats_rel_wind.set_index("Estadísticas")

    df_stats_rel_wind.loc["Mínima rel. (Rango sel.)", "Velocidad [Km/h]"] = df[
        "Vel."
    ].min()
    df_stats_rel_wind.loc["Mínima rel. (Rango sel.)", "Fecha"] = df["Vel."].idxmin()
    df_stats_rel_wind.loc["Mínima Max. rel. (Rango sel.)", "Velocidad [Km/h]"] = df[
        "Vel."
    ].max()
    df_stats_rel_wind.loc["Mínima Max. rel. (Rango sel.)", "Fecha"] = df[
        "Vel."
    ].idxmax()
    df_stats_rel_wind.loc["Máxima rel. (Rango sel.)", "Velocidad [Km/h]"] = df[
        "Vel."
    ].max()
    df_stats_rel_wind.loc["Máxima rel. (Rango sel.)", "Fecha"] = df["Vel."].idxmax()
    df_stats_rel_wind.loc["Máxima Min. rel. (Rango sel.)", "Velocidad [Km/h]"] = df[
        "Vel."
    ].min()
    df_stats_rel_wind.loc["Máxima Min. rel. (Rango sel.)", "Fecha"] = df[
        "Vel."
    ].idxmin()


    df_stats_rel_wind["Fecha"] = pd.to_datetime(df_stats_rel_wind["Fecha"]).dt.strftime(
        "%d-%m-%Y"
    )
    df_stats_rel_wind["Velocidad [Km/h]"] = df_stats_rel_wind["Velocidad [Km/h]"].apply(
        lambda x: f"{x:.1f}"
    )

    return df_stats_rel_wind

def wind_heatmap_max_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df.drop("Interanual")