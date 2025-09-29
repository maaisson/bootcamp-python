# Calcular desvio padrão de valores em uma lista
from typing import List

def calcular_desvio(valores: List[float]) -> float:
    if not valores:
        raise ValueError("A lista de valores não pode ser vazia.")
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

# Exemplo de uso
valores = [10, 20, 30, 40, 50]
desvio = calcular_desvio(valores)
print(f"Desvio padrão dos valores {valores}: {desvio}")