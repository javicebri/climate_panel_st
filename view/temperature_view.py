from controller.temperature_controller import max_temperature_controller

import pandas as pd


def show():
    max_temperature_serie_plot()


def max_temperature_serie_plot(max_temperature_serie: pd.DataFrame):
    max_temperature_serie = max_temperature_controller()
