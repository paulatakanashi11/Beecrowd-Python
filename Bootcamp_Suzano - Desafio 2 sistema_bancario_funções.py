import textwrap

def menu():
    menu = """
    [1] = Depósito
    [2] = Saque
    [3] = Extrato
    [4] = Cadastrar Usuário
    [5] = Cadastrar Conta Bancária
    [6] = Sair
    """
    return input(textwrap.dedent(menu))


# Função depósito: deve receber os argumentos apenas por posição (ARGUMENTOS: saldo, valor, extrato |RETORNO: saldo e extrato)
def deposito(saldo, valor, extrato_conta, /):
    if valor > 0:
        saldo += valor
        extrato_conta += f"Depósito de R$ {valor:.2f} realizado com sucesso.\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")
    return saldo, extrato_conta


# Função saque: deve receber os argumentos apenas por nome. (ARGUMENTOS: saldo, valor, extrato, limite, numero_saques, limite_saques | RETORNO: saldo e extrato)
def saque(*, saldo, valor, extrato_conta, limite, numero_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente para sacar esse valor!")
    elif valor > limite: 
        print("Você excedeu o limite de R$500,00 por saque!")
    elif numero_saques < 3:
        saldo -= valor
        numero_saques += 1
        extrato_conta += f"Saque de R$ {valor:.2f} realizado com sucesso.\n"
        print(f"Valor sacado: R$ {valor} com sucesso!")
    else:
        print("Você excedeu o limite de 3 saques diários! Tente outro dia.")
    return saldo, extrato_conta, numero_saques


# Função Extrato: deve receber os argumentos por posição e nome (saldo, argumentos nomeados: extrato)
def extrato(saldo, /, *, extrato_conta):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
    return extrato_conta


# Criar usuário: o programa deve cadastrar os usuários em uma lista
def criar_usuario(nome, nascimento, cpf, endereco, usuarios):
    # Verifica se o CPF já existe
    cpf = cpf.replace(".", "").replace("-", "")  # Remove pontos e traços
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado! Não é possível cadastrar o mesmo CPF.")
        return

    # Cria o dicionário do usuário
    usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


# Criar conta: deve armazenar contas em uma lista
def criar_conta(cpf, usuarios, contas, numero_conta):
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado!")
        return numero_conta
    nova_conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(nova_conta)
    numero_conta += 1
    print(f"Conta criada com sucesso! Agência: 0001, Conta: {nova_conta['numero_conta']}")
    return numero_conta


def main():
    contas = []
    numero_conta = 1
    usuarios = []
    saldo = 0
    extrato_conta = ""
    limite_saque = 500
    numero_saques = 0  # Inicializando o contador de saques

    while True: 
        opcao = menu()

        if opcao == "1":
            valor = float(input("Qual valor você deseja depositar? "))
            saldo, extrato_conta = deposito(saldo, valor, extrato_conta)

        elif opcao == "2":
            valor = float(input("Qual valor você deseja sacar? "))
            saldo, extrato_conta, numero_saques = saque(saldo=saldo, valor=valor, extrato_conta=extrato_conta, limite=limite_saque, numero_saques=numero_saques)

        elif opcao == "3":
            extrato(saldo, extrato_conta=extrato_conta)
        
        elif opcao == "4":
            nome = input("Nome: ")
            nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            criar_usuario(nome, nascimento, cpf, endereco, usuarios)

        elif opcao == "5":
            cpf = input("Qual é o CPF do usuário? ")
            numero_conta = criar_conta(cpf, usuarios, contas, numero_conta)

        elif opcao == "6":
            print("Saindo...")
            break

        else: 
            print("Opção inválida. Tente novamente!")


# Chama a função principal
main()
