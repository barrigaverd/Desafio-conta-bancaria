menu = """

[d] Depositar
[s] Sacar
[e] Extrato

[l] Listar contas
[n] Novo usuário
[c] Nova conta

[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
numero_conta = 0



def deposito(saldo, valor, extrato):
    #depositando 50
    if valor > 0: #True
        saldo += valor #saldo = 50
        print("Depósito realizado com sucesso!") 
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    #verificações
    #simulação com valor de 100 de saque
    excedeu_saldo = valor > saldo #False
    excedeu_limite = valor > limite #False
    excedeu_saques = numero_saques >= limite_saques #False

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0: #True
        saldo -= valor #saldo = 400
        extrato += f"Saque: R$ {valor:.2f}\n" 
        numero_saques += 1 #numero_saques = 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#criar usuario(cliente do banco)
def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return print("CPF já cadastrado!")
    
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

#vincular com o usuario
def conta_bancaria(agencia, numero_conta, usuarios):
    numero_conta += 1

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuarios': usuarios,
    }

    return  conta, numero_conta


def buscar_usuario(cpf, usuarios):
    usuarios_buscados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_buscados[0] if usuarios_buscados else None

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        texto_exibir = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuarios']['nome']}
        """
        print(texto_exibir)


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "l":
        listar_contas(contas)
    
    elif opcao == "n":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário: ")
        cpf = input("Informe o CPF do usuário: ")
        endereco = input("Informe o endereço do usuário: ")
        cadastrar_usuario(usuarios,nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        usuario = buscar_usuario(cpf, usuarios)

        if usuario:
            print("Usuário encontrado!")
        else:
            print("Usuário não encontrado!")
            continue

        agencia = "0001"
        conta, numero_conta = conta_bancaria(agencia, numero_conta, usuario)

        if conta:
            print("Conta criada com sucesso!")
            contas.append(conta)
        else:
            print("Conta não criada!")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
