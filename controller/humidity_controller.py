from model.humidity_model import (
    get_max_humidity_serie,
    humidity_relative_records_table_model,
    humidity_absolute_records_table_model,
    humidity_max_summary_table_model,
    humidity_min_summary_table_model,
)

import pandas as pd


def max_humidity_controller():
    max_humidity_serie = get_max_humidity_serie()
    return max_humidity_serie


def humidity_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return humidity_relative_records_table_model(df)


def humidity_absolute_records_table_controller() -> pd.DataFrame:
    return humidity_absolute_records_table_model()


def humidity_max_summary_table_controller() -> pd.DataFrame:
    return humidity_max_summary_table_model()


def humidity_min_summary_table_controller() -> pd.DataFrame:
    return humidity_min_summary_table_model()
