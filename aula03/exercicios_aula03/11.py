# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite algo (ou 'sair' para terminar): ")
    if entrada.lower() != "sair":
        dados.append(entrada)