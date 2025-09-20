constante_bonus = 1000
nome_valido = False
bonus_valido = False
salario_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        
        if len(nome) == 0:
            raise ValueError("O nome não pode ser vazio.")
            exit()
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode conter números.")
            exit()
        else:
            print(f"Olá {nome}, seja bem-vindo(a)!")
            nome_valido = True
            
    except ValueError as e:
        print(e)
        exit()

while not salario_valido:        
    try:
        salario = float(input(f"Agora {nome}, Digite o valor do seu salário: "))
        
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        else:
            salario_valido = True
        
    except ValueError:
        print("Por favor, insira um valor numérico válido para o salário.")
        exit()

while not bonus_valido:
    try:
        bonus = float(input(f"Por fim {nome}, Digite o valor do bônus recebido (pode ser em %): "))

        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Por favor, insira um valor numérico válido para o bônus.")
        exit()
        
    bonus_recebido = constante_bonus + salario * bonus

    print(f"{nome}, seu salário é R$ {salario:.2f} e o bônus recebido é R$ {bonus_recebido:.2f}.")