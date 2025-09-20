# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

max_tentativas = 5
tentativa = 0

while tentativa <= max_tentativas:
    print(f"Tentativa {tentativa + 1} de {max_tentativas}")
    # Simula uma tentativa de conexão (substitua por código real de conexão)
    sucesso = False  # Altere para True para simular uma conexão bem-sucedida

    if sucesso:
        print("Conexão bem-sucedida!")
        break
    else:
        print("Falha na conexão. Tentando novamente...")
        tentativa += 1
else:
    print("Número máximo de tentativas atingido. Não foi possível conectar.")