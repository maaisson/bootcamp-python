# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

constante_bonus = 1000

nome = input("Digite seu nome: ")
salario = float(input(f"Agora {nome}, Digite o valor do seu salário: "))
bonus = float(input(f"Por fim {nome}, Digite o valor do bônus recebido (pode ser em %): "))

calculo_kpi = constante_bonus + salario * bonus

print(f"Então {nome}, o seu bonus foi de {calculo_kpi}")