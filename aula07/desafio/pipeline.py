from etl import ler_csv, processar_dados, calcular_vendas_categoria

if __name__ == "__main__":
    nome_arquivo = 'D:\\Estudos\\bootcamp python\\aula07\\desafio\\vendas.csv'
    dados = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados)
    vendas_por_categoria = calcular_vendas_categoria(dados_processados)
    
    for categoria, total in vendas_por_categoria.items():
        print(f"Categoria: {categoria}, Total de Vendas: R$ {total:.2f}")