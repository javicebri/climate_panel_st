from model.temperature_model import (
    get_max_temperature_serie,
    temperature_relative_records_table_model,
    temperature_absolute_records_table_model,
    temperature_max_summary_table_model,
    temperature_med_summary_table_model,
    temperature_min_summary_table_model,
    temperature_heatmap_max_model,
    temperature_heatmap_min_model,
    temperature_trend_max_model,
    temperature_trend_min_model
)

import pandas as pd


def max_temperature_controller():
    max_temperature_serie = get_max_temperature_serie()
    return max_temperature_serie


def temperature_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return temperature_relative_records_table_model(df)


def temperature_absolute_records_table_controller() -> pd.DataFrame:
    return temperature_absolute_records_table_model()


def temperature_max_summary_table_controller() -> pd.DataFrame:
    return temperature_max_summary_table_model()


def temperature_med_summary_table_controller() -> pd.DataFrame:
    return temperature_med_summary_table_model()


def temperature_min_summary_table_controller() -> pd.DataFrame:
    return temperature_min_summary_table_model()


def temperature_heatmap_max_controller() -> pd.DataFrame:
    df = temperature_max_summary_table_controller()
    return temperature_heatmap_max_model(df)


def temperature_heatmap_min_controller() -> pd.DataFrame:
    df = temperature_min_summary_table_controller()
    return temperature_heatmap_min_model(df)

def temperature_trend_max_controller() -> pd.DataFrame:
    return temperature_trend_max_model()


def temperature_trend_min_controller() -> pd.DataFrame:
    return temperature_trend_min_model()
