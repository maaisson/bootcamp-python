# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input("Digite um texto: ")
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
        
print(contagem_palavras)    
