
# Variáveis globais
usuarios = []
contas = []
saldo = 0
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
numero_conta = 1
extrato = []

# Funções principais

def criar_usuario(nome, data_nascimento, cpf, endereco):
    """Cria um novo usuário e adiciona à lista de usuários."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado.")
        return None
    
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuario

def criar_conta(usuario):
    """Cria uma nova conta para um usuário e adiciona à lista de contas."""
    global numero_conta
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    numero_conta += 1
    print(f"Conta criada com sucesso para {usuario['nome']}!")
    return conta

# Função para listar todas as contas
def listar_contas():
    """Lista todas as contas cadastradas no sistema."""
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("\nListagem de Contas:")
        for conta in contas:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {usuario['nome']}, CPF: {usuario['cpf']}")
        print("\n")

def deposito(valor):
    """Realiza um depósito na conta e atualiza o saldo e o extrato."""
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")
    return saldo

def saque(valor):
    """Realiza um saque da conta e atualiza o saldo, o extrato e o número de saques."""
    global saldo, numero_saques, limite_saque, LIMITE_SAQUES_DIARIOS, extrato
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"Não é possível sacar valores acima de R$ {limite_saque:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de saque inválido.")
    return saldo

def exibir_extrato():
    """Exibe o extrato bancário e o saldo atual."""
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato Bancário:")
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Menu principal
while True:
    print("Bem-vindo ao Banco!")
    print("[1] Criar Usuário")
    print("[2] Criar Conta Corrente")
    print("[3] Depositar")
    print("[4] Sacar")
    print("[5] Extrato")
    print("[6] Listar Contas")
    print("[7] Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = {
            'logradouro': input("Digite o logradouro: "),
            'numero': input("Digite o número: "),
            'bairro': input("Digite o bairro: "),
            'cidade': input("Digite a cidade: "),
            'estado': input("Digite o estado (sigla): ")
        }
        criar_usuario(nome, data_nascimento, cpf, endereco)
        
    elif opcao == "2":
        cpf_usuario = input("Digite o CPF do usuário para criar a conta: ")
        usuario = next((u for u in usuarios if u['cpf'] == cpf_usuario), None)
        if usuario:
            criar_conta(usuario)
        else:
            print("Usuário não encontrado.")
    
    elif opcao == "3":
        valor = float(input("Digite o valor do depósito: R$ "))
        saldo = deposito(valor)
    
    elif opcao == "4":
        valor = float(input("Digite o valor do saque: R$ "))
        saldo = saque(valor)
    
    elif opcao == "5":
        exibir_extrato()

    elif opcao == "6":
        listar_contas()    
    
    elif opcao == "7":
        print("Obrigado por utilizar o banco. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
