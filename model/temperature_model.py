import pandas as pd
import streamlit as st


def get_max_temperature_serie():
    pass


def temperature_relative_records_table_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataframe with the records for the input df
    Params:
        df (pd.DataFrame): input dataframe to compute statistics
    Returns:
        pd.DataFrame with records
    """

    df_stats_rel_temp = pd.DataFrame({'Estadísticas': ['Media td1 mínima rel. (Rango sel.)', 'Media td1 máxima rel. (Rango sel.)',
                                               'Mínima rel. (Rango sel.)', 'Mínima Max. rel. (Rango sel.)', 
                                               'Máxima rel. (Rango sel.)', 'Máxima Min. rel. (Rango sel.)',
                                               'Min. amplitud rel. (Rango sel.)', 'Max. amplitud rel. (Rango sel.)'], 
                              'Fecha': [0,0,0,0,0,0,0,0],
                              'Temperatura [ºC]': [0,0,0,0,0,0,0,0]})
    
    df_stats_rel_temp = df_stats_rel_temp.set_index('Estadísticas')

    df_stats_rel_temp.loc['Media td1 mínima rel. (Rango sel.)','Temperatura [ºC]'] = df['T. med1.'].min()
    df_stats_rel_temp.loc['Media td1 mínima rel. (Rango sel.)','Fecha'] = df['T. med1.'].idxmin()
    df_stats_rel_temp.loc['Media td1 máxima rel. (Rango sel.)','Temperatura [ºC]'] = df['T. med1.'].max()
    df_stats_rel_temp.loc['Media td1 máxima rel. (Rango sel.)','Fecha'] = df['T. med1.'].idxmax()
    df_stats_rel_temp.loc['Mínima rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Min.'].min()
    df_stats_rel_temp.loc['Mínima rel. (Rango sel.)','Fecha'] = df['T. Min.'].idxmin()
    df_stats_rel_temp.loc['Mínima Max. rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Min.'].max()
    df_stats_rel_temp.loc['Mínima Max. rel. (Rango sel.)','Fecha'] = df['T. Min.'].idxmax()
    df_stats_rel_temp.loc['Máxima rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Max.'].max()
    df_stats_rel_temp.loc['Máxima rel. (Rango sel.)','Fecha'] = df['T. Max.'].idxmax()
    df_stats_rel_temp.loc['Máxima Min. rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Max.'].min()
    df_stats_rel_temp.loc['Máxima Min. rel. (Rango sel.)','Fecha'] = df['T. Max.'].idxmin()    
    df_stats_rel_temp.loc['Min. amplitud rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Amp.'].min()
    df_stats_rel_temp.loc['Min. amplitud rel. (Rango sel.)','Fecha'] = df['T. Amp.'].idxmin()
    df_stats_rel_temp.loc['Max. amplitud rel. (Rango sel.)','Temperatura [ºC]'] = df['T. Amp.'].max()
    df_stats_rel_temp.loc['Max. amplitud rel. (Rango sel.)','Fecha'] = df['T. Amp.'].idxmax()

    return df_stats_rel_temp

