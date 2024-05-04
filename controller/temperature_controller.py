from model.temperature_model import get_max_temperature_serie


def max_temperature_controller():
    max_temperature_serie = get_max_temperature_serie()
    return max_temperature_serie
