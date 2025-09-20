# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 4, "parar", 8, 9, 10]
i = 0

while i < len(itens):
    if itens[i] == "parar":
        print("Valor 'parar' encontrado. Encerrando o loop.")
        break
    print(f"Processando item: {itens[i]}")
    i += 1
    
