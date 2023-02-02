import pandas as pd

def dados_tratados():
    # coleta dos dados tratados
    global df_raw
    arquivo_base = "dataset_compras.xlsx - Sheet1.csv"
    df_raw = pd.read_csv(arquivo_base)

    return df_raw