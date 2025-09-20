# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e 
# tenha fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

if not (18 <= idade <= 65):
    print("Erro: Idade fora do intervalo permitido.")
elif "@" not in email or "." not in email:
    print("Erro: Email inválido.")
else:
    print("Dados de usuário válidos")