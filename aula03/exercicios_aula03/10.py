# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletronicos", "valor": 1000},
    {"categoria": "moveis", "valor": 500},
    {"categoria": "eletronicos", "valor": 1500},
    {"categoria": "roupas", "valor": 300}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)