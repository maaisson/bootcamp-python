# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

constante_bonus = 1000

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
        
except ValueError as e:
    print(e)
    exit()
    
try:
    salario = float(input(f"Agora {nome}, Digite o valor do seu salário: "))
    
    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")
    
except ValueError:
    print("Por favor, insira um valor numérico válido para o salário.")
    exit()


try:
    bonus = float(input(f"Por fim {nome}, Digite o valor do bônus recebido (pode ser em %): "))

    if bonus < 0:
        raise ValueError("O bônus não pode ser negativo.")
except ValueError:
    print("Por favor, insira um valor numérico válido para o bônus.")
    exit()
    
bonus_recebido = constante_bonus + salario * bonus

print(f"{nome}, seu salário é R$ {salario:.2f} e o bônus recebido é R$ {bonus_recebido:.2f}.")