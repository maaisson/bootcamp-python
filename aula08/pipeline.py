import os
from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_data = os.path.join('aula08', 'data')
prompt_usuario = "Digite os formatos de saída desejados (csv, parquet) separados por vírgula: "
entrada_usuario = input(prompt_usuario)

formato_saida = [formato.strip() for formato in entrada_usuario.split(',') if formato.strip() in ['csv', 'parquet']]

pipeline_calcular_kpi_de_vendas_consolidado(pasta_data, formato_saida)