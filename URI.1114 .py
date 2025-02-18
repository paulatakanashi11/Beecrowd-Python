#URI.1114 - Senha Fixa

SENHA_OK = '2002'  

while True:  # Loop infinito, até o usuário acertar a senha
    senha = input()  # Lê a senha do usuário
    if senha == SENHA_OK:
        print("Acesso Permitido")
        break  # Sai do loop quando a senha estiver correta
    else:
        print("Senha Invalida")
