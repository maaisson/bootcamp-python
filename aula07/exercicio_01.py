## Calcular media de valores em uma lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    if not valores:
        raise ValueError("A lista de valores não pode ser vazia.")
    return sum(valores) / len(valores)

# Exemplo de uso
valores = [10, 20, 30, 40, 50]
media = calcular_media(valores)
print(f"A média dos valores {valores} é {media}")