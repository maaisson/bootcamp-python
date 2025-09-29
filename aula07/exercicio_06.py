# encontrar valores ausentes em uma sequência
from typing import List

def encontrar_valores(sequencia: List[int]) -> List[int]:
    if not sequencia:
        return []
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return sorted(list(completo - set(sequencia)))

# Exemplo de uso
sequencia = [1, 2, 4, 6, 7, 9]
valores_ausentes = encontrar_valores(sequencia)
print(f"Valores ausentes na sequência {sequencia}: {valores_ausentes}")