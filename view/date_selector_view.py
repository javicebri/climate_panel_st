import streamlit as st
from assets.texts import texts


def show_date_selector_view() -> None:
    """
    Selector of the initial and final date to be represented
    """
    st.session_state["df_out"]
    min_date = st.session_state["df_out"].index[0].date()
    max_date = st.session_state["df_out"].index[-1].date()

    init_date, last_date = st.slider(
        texts.date_selector,
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    st.session_state["init_date"] = init_date
    st.session_state["last_date"] = last_date
