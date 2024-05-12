import pandas as pd
import streamlit as st


def get_max_temperature_serie():
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


def calculate_max_temperature_anual_serie() -> pd.Series:
    """
    Return a serie with the med temp of each year, only consider year with all of month with data
    TODO: Esta operación debe ser incluida en la generación de tablas (preprocesado, para reducir carga computacional)
    """
    max_summary_df = st.session_state["summary_max_temp_dict"]
    # Drop rows with NaN
    max_summary_df = max_summary_df.dropna()
    max_summary_df =max_summary_df.drop("Interanual")
    max_med_df = max_summary_df.mean(axis=1)
    return (max_med_df)


def calculate_min_temperature_anual_serie() -> pd.Series:
    """
    Return a serie with the med temp of each year, only consider year with all of month with data
    TODO: Esta operación debe ser incluida en la generación de tablas (preprocesado, para reducir carga computacional)
    """
    min_summary_df = st.session_state["summary_min_temp_dict"]
    # Drop rows with NaN
    min_summary_df = min_summary_df.dropna()
    min_summary_df =min_summary_df.drop("Interanual")
    min_med_df = min_summary_df.mean(axis=1)
    return (min_med_df)


def temperature_trend_max_model() -> tuple:
    # TODO: Falta añadir los puntos scatter de las medias anuales
    # max_med_df = calculate_max_temperature_anual_serie()
    df = st.session_state["df_input_trend"]
    # max_med_df = max_med_df.reindex(df.index)
    # df['Anual_max_mean'] = max_med_df
    return df


def temperature_trend_min_model() -> pd.DataFrame:
    # TODO: Falta añadir los puntos scatter de las medias anuales
    # min_med_df = calculate_min_temperature_anual_serie()
    df = st.session_state["df_input_trend"]
    # min_med_df = min_med_df.reindex(df.index)
    # df['Anual_min_mean'] = min_med_df
    return df


def temperature_max_summary_table_model():
    max_summary_df = st.session_state["summary_max_temp_dict"].map(format_value)
    max_summary_df.index = max_summary_df.index.map(format_value)
    return max_summary_df


def temperature_med_summary_table_model():
    med_summary_df = st.session_state["summary_med_temp_dict"].map(format_value)
    med_summary_df.index = med_summary_df.index.map(format_value)
    return med_summary_df


def temperature_min_summary_table_model():
    min_summary_df = st.session_state["summary_min_temp_dict"].map(format_value)
    min_summary_df.index = min_summary_df.index.map(format_value)
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
            "Temperatura [ºC]": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
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


def temperature_heatmap_max_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df.drop("Interanual")


def temperature_heatmap_min_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df.drop("Interanual")
