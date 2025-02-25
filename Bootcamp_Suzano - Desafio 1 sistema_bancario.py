menu = """
[1] = Depósito
[2] = Saque
[3] = Extrato
[4] = Sair

"""

saldo = 0
limite_saque = 500
limite_diario = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual valor você deseja depositar? "))
        saldo += valor 
        print(f"Valor depositado: {valor} com sucesso!")

    elif opcao == "2":
        valor = float(input("Qual valor você deseja sacar? "))
        if valor > saldo:
            print("Você não tem saldo suficiente para sacar esse valor!")
        elif valor > limite_saque: 
            print("Você excedeu o limite de R$500,00 por saque!")
        elif limite_diario < 3:
                saldo -= valor
                limite_diario += 1
                print(f"Valor sacado: {valor} com sucesso!")
        else:
            print("Voce excedeu o limite de 3 saques diários! Tente outro dia")

    elif opcao == "3":
        print(f"Seu saldo atual é: {saldo}")
    elif opcao == "4":
        break
    else: 
        print("Opção inválida. Tente novamente!")
