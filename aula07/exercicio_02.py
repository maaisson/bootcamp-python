# Filtrar dados acima de um limite
from typing import List

def filtrar_acima_limite(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# Exemplo de uso
valores = [10, 20, 30, 40, 50]
limite = 25
valores_filtrados = filtrar_acima_limite(valores, limite)
print(f"Valores acima do limite {limite}: {valores_filtrados}")