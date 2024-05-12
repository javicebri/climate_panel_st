from model.precipitation_model import (
    get_precipitation_serie,
    precipitation_relative_records_table_model,
    precipitation_absolute_records_table_model,
    precipitation_summary_table_model,
    precipitation_heatmap_model
)

import pandas as pd


def precipitation_controller():
    precipitation_serie = get_precipitation_serie()
    return precipitation_serie


def precipitation_relative_records_table_controller(df: pd.DataFrame) -> pd.DataFrame:
    return precipitation_relative_records_table_model(df)


def precipitation_absolute_records_table_controller() -> pd.DataFrame:
    return precipitation_absolute_records_table_model()


def precipitation_summary_table_controller() -> pd.DataFrame:
    return precipitation_summary_table_model()


def precipitation_heatmap_controller() -> pd.DataFrame:
    df = precipitation_summary_table_controller()
    return precipitation_heatmap_model(df)
