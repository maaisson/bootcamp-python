from typing import List

def ler_csv(nome_arquivo:str) -> List[dict]:
    dados = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            registro = {cabecalho[i]: valores[i] for i in range(len(cabecalho))}
            dados.append(registro)
    return dados

def processar_dados(dados: List[dict]) -> List[dict]:
    for registro in dados:
        if 'Produto' in registro:
            registro['Produto'] = str(registro['Produto'])
        if 'Quantidade' in registro:
            registro['Quantidade'] = int(registro['Quantidade'])
        if 'Venda' in registro:
            registro['Venda'] = float(registro['Venda'])
    return dados

def calcular_vendas_categoria(dados: List[dict]) -> dict:
    vendas_categoria = {}
    for registro in dados:
        categoria = registro.get('Categoria', 'Desconhecida')
        venda = registro.get('Venda', 0.0)
        if categoria in vendas_categoria:
            vendas_categoria[categoria] += venda
        else:
            vendas_categoria[categoria] = venda
    return vendas_categoria

