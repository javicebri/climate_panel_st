from model.wind_model import (
    get_max_wind_serie,
    wind_relative_records_table_model,
    wind_absolute_records_table_model,
    wind_max_summary_table_model,
    wind_heatmap_max_model
)

import pandas as pd


def max_wind_controller():
    max_wind_serie = get_max_wind_serie()
    return max_wind_serie


def wind_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return wind_relative_records_table_model(df)


def wind_absolute_records_table_controller() -> pd.DataFrame:
    return wind_absolute_records_table_model()


def wind_max_summary_table_controller() -> pd.DataFrame:
    return wind_max_summary_table_model()


def wind_heatmap_max_controller() -> pd.DataFrame:
    df = wind_max_summary_table_controller()
    return wind_heatmap_max_model(df)
