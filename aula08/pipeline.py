import os
from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_data = os.path.join('aula08', 'data')
formato_saida: list = ['csv', 'parquet']

pipeline_calcular_kpi_de_vendas_consolidado(pasta_data, formato_saida)