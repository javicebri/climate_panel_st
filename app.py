import streamlit as st

from view import (
    date_selector_view,
    temperature_view,
    pressure_view,
    humidity_view,
    wind_view,
    precipitation_view,
)

from model.session import load_data_session

from streamlit_option_menu import option_menu
from global_vars import (
    menu_icon,
    temperature_icon,
    pressure_icon,
    humidity_icon,
    wind_icon,
    precipitation_icon,
    escudo_path,
)

from assets.texts import texts

from assets.css.styles import main_style_css, menu_style_css

load_data_session()


st.markdown(
    main_style_css,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    "<h2 style='font-size: 40px;'>Panel de datos climáticos</h2>",
    unsafe_allow_html=True,
)

text_col, img_col = st.sidebar.columns([2, 1])

with text_col:
    st.write("# Valdepeñas de la Sierra")

with img_col:
    st.image(escudo_path, width=100)

# Menu sidebar
with st.sidebar:
    selected = option_menu(
        menu_title=texts.main_menu,
        options=[
            texts.menu_temperature,
            texts.menu_pressure,
            texts.menu_humidity,
            texts.menu_wind,
            texts.menu_precipitation,
        ],
        icons=[
            temperature_icon,
            pressure_icon,
            humidity_icon,
            wind_icon,
            precipitation_icon,
        ],
        menu_icon=menu_icon,
        default_index=0,
        manual_select=0,
        styles=menu_style_css,
    )

################
# Temperature  #
################

if selected == texts.menu_temperature:
    date_selector_view.show_date_selector_view()
    temperature_view.show()


################
# Pressure     #
################

if selected == texts.menu_pressure:
    pressure_view.show()

################
# Humidity     #
################

if selected == texts.menu_humidity:
    humidity_view.show()

################
# Wind         #
################

if selected == texts.menu_wind:
    wind_view.show()

#################
# Precipitation #
#################

if selected == texts.menu_precipitation:
    precipitation_view.show()
