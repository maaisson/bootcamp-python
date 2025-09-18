# %%
data = input("Digite a data (dd/mm/aaaa): ")
dataFormatada = data.split("/")
print("dia:", dataFormatada[0])
print("mês:", dataFormatada[1])
print("ano:", dataFormatada[2])

# %%
while True:
    data = input("Digite a data (dd/mm/aaaa): ")
    try:    
        dataFormatada = data.split("/")
        dia = int(dataFormatada[0])
        mes = int(dataFormatada[1])
        ano = int(dataFormatada[2])
        
        if dia and mes and ano:
            print("dia:", dia)
            print("mês:", mes)
            print("ano:", ano)
            break
        else:
            raise ValueError("Partes da data estão vazias ou inválidas.")
    except (IndexError, ValueError):
        print("Formato inválido, tente novamente no formato dd/mm/aaaa.")
