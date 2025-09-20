# Objetivo: Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando.

usuarios = [
    {"nome": "Lucas", "email": "lucas@example.com"},
    {"nome": "Maria", "email": None},
    {"nome": "João", "email": "joao@example.com"}    
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)