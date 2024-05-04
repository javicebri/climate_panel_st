from model.temperature_model import (
    get_max_temperature_serie,
    temperature_relative_records_table_model,
    temperature_absolute_records_table_model
)

import pandas as pd


def max_temperature_controller():
    max_temperature_serie = get_max_temperature_serie()
    return max_temperature_serie


def temperature_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return temperature_relative_records_table_model(df)

def temperature_absolute_records_table_controller() -> pd.DataFrame:
    return temperature_absolute_records_table_model()
