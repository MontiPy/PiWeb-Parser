import pandas as pd


def convert_in2mm(x):
    return x*25.4

def extract_CMM(df):
    df_ = df.copy()[['Characteristic', 'K1 Measured value', 'K53 Order number', 'K4 Time/Date',
                     'K2101 Nominal value', 'K2110 Lower limit', 'K2111 Upper limit', 'K2142 Unit']]
    df_ = df_.astype({'Characteristic': 'str',
                      'K1 Measured value': 'float64',
                      'K53 Order number': 'str',
                      'K4 Time/Date': 'datetime64[ns]',
                      'K2101 Nominal value': 'float64',
                      'K2110 Lower limit': 'float64',
                      'K2111 Upper limit': 'float64',
                      'K2142 Unit': 'str'})
    df_pivot = df_.pivot_table(index=['K53 Order number', 'K4 Time/Date'],
                               columns='Characteristic', values='K1 Measured value')
    df_pivot = df_pivot.reset_index()
    df_pivot = df_pivot.sort_values(by="K4 Time/Date", ascending=True)
    return df_pivot
