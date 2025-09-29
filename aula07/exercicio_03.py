# Contar valores únicos em uma lista
from typing import List

def contar_valores_unicos(valores: List[int]) -> int:
    return len(set(valores))

# Exemplo de uso
valores = [1, 2, 2, 3, 4, 4, 4, 5]
quantidade_unicos = contar_valores_unicos(valores)
print(f"Quantidade de valores únicos em {valores}: {quantidade_unicos}")