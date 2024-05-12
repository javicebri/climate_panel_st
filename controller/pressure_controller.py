from model.pressure_model import (
    get_max_pressure_serie,
    pressure_relative_records_table_model,
    pressure_absolute_records_table_model,
    pressure_max_summary_table_model,
    pressure_min_summary_table_model,
)

import pandas as pd


def max_pressure_controller():
    max_pressure_serie = get_max_pressure_serie()
    return max_pressure_serie


def pressure_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return pressure_relative_records_table_model(df)


def pressure_absolute_records_table_controller() -> pd.DataFrame:
    return pressure_absolute_records_table_model()


def pressure_max_summary_table_controller() -> pd.DataFrame:
    return pressure_max_summary_table_model()


def pressure_min_summary_table_controller() -> pd.DataFrame:
    return pressure_min_summary_table_model()
