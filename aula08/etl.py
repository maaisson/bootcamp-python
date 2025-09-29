import pandas as pd
import os
import glob

def extrair_dados_e_consolidar(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_novo = df.copy()
    df_novo['Total'] = df_novo['Quantidade'] * df_novo['Venda']
    return df_novo

def carregar_dados(df:pd.DataFrame, formato_saida:list):
    if 'csv' in formato_saida:
        df.to_csv('vendas_total.csv', index=False)
    if 'parquet' in formato_saida:
        df.to_parquet('vendas_total.parquet', index=False)
        
def pipeline_calcular_kpi_de_vendas_consolidado(pasta:str, formato_saida:list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_saida)

    