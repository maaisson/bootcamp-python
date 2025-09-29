# Converter Celsius para Fahrenheit
from typing import List

def celsius_para_fahrenheit(celsius: List[float]) -> List[float]:
    return [(temp * 9/5) + 32 for temp in celsius]

# Exemplo de uso
celsius = [0, 20, 37, 100]
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"Temperaturas em Celsius: {celsius}")
print(f"Temperaturas em Fahrenheit: {fahrenheit}")