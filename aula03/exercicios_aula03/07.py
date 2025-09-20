# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50, 60]

minimo = min(numeros)
maximo = max(numeros)

numeros_normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(numeros_normalizados)
