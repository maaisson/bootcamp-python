# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1, 21)
pares = [x for x in numeros if x % 2 == 0]

print(pares)