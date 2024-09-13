opcao = 0

menuInicial = """
[1] - depositar | [4] - saques restantes
[2] - sacar     | [5] - cadastrar cliente
[3] - extrato   | [6] - criar conta corrente
[7] - exibir contas cadastradas
[8] - sair 
==>"""

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
saques = 0
limiteSaques = 3
clientes=[]
contas=[]

def criarCliente(clientes):
    try:
        cpf=int(input("informe seu CPF (apenas numeros): "))
        usuario = filtrarUsuario(cpf,clientes)
        if usuario:
            print("Usuario ja existente com esse CPF")
            print(filtrarUsuario(cpf,clientes))
            return
    except ValueError:
        print("""apenas numeros. 
retornando para o menu inicial""")
        return
   
    nome=input("seu nome completo: ")
    nascimento= input("sua data de nascimento(dd/mm/aaaa): ")
    endereco=input("informe seu endereço (logradouro,numero - bairro - cidade/sigla do estado): ")

    clientes.append({'nome': nome, 'nascimento':nascimento,'cpf':cpf, 'endereco':endereco})

    print("cliente cadastrado com sucesso :D")

def filtrarUsuario(cpf,clientes):
    clientesFiltrados = [x for x in clientes if x["cpf"] == cpf] # 'x' é uma variavel criada para percorrer a lista 'clientes',
    # 'x' vira um coringa pra buscar se na posiçao "cpf" = cpf. isso tudo é um filtro para retornar o dicionario inteiro, se 'cpf' = cpf
    return clientesFiltrados[0] if clientesFiltrados else None # aqui retorna clientes filtrados na posiçao 0, n necessariamente 'cpf', 
    # caso clientes filtrados nao estiver vazio
    
def criarContaCorrente(AGENCIA,clientes,contas):
    numeroConta = len(contas)+1
    conta = criarConta(AGENCIA,numeroConta,clientes)

    if conta:
        print(f"conta nova criada: {conta}")
        contas.append(conta)

def criarConta(agencia,numeroConta,clientes):
    try:
        cpf = int(input("informe o cpf do usuario"))
        usuario = filtrarUsuario(cpf,clientes)
        
        if usuario:
            print("\nconta corrente criada com sucesso!")
            return {'agencia':agencia, "numeroConta":numeroConta, 'usuario':usuario}
        print("\nUsuario nao encontrado, retornando ao menu principal")

    except ValueError:
        print("""apenas numeros. 
retornando para o menu inicial""")    
        return

def contasExistentes(contas):
    for conta in contas:
        print(f"""-------------------------------------------
        agencia: {conta['agencia']}
        C/C: {conta['numeroConta']}
        titular: {conta['usuario']['nome']}""")
    print("-" * 100 )

def excluirConta():
    print('x')

def depositar(saldo,extrato,/): # '/' depois faz com que tudo antes seja interpretado apenas pela posicao do argumento
    try: 
        valor = float(input("valor a depositar:"))
        if  valor > 0:            
            saldo += valor
            extrato +=  f"deposito de R${valor:.2f}\n"
            print(f"valor depositado: R${valor:.2f}")
            print(f"saldo = R${saldo:.2f}")
        else: print("valor do deposito precisa ser positivo")
        return saldo, extrato
    except ValueError: print("valor precisa ser um numero")

def sacar(*,saldo, extrato): # '*' faz cpm que tudo depois seja interpretado apenas por nome. EX: saldo=saldo
    try:
        valor = float(input("valor a sacar:"))
        if  valor > saldo: 
            print ("saldo insuficiente")
            return saldo, extrato
        
        if  valor > 0 and valor <= 500:
            saldo -= valor
            extrato +=  f"saque de R${valor:.2f}\n" 
            print(f"valor sacado: R${valor:.2f}")
            print(f"saldo = R${saldo:.2f}") 
        elif valor > 500:
            print("valor do saque precisa ser ate R$500,00")          
        else: print("valor do saque nao pode ser negativo")
        return saldo, extrato
    except ValueError: print("valor precisa ser um numero")

def historico(saldo,/,*,extrato):
    print("\n=============EXTRATO=============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("=================================")

while opcao != 8:
    
    try:
        opcao = int(input(menuInicial))

        if  opcao == 1: 
            result = depositar(saldo, extrato)
            saldo = result[0] 
            extrato = result [1] 

        elif opcao == 2:
            if saques >= 3:
                print("limite de saques atingido")
            else:
                result = sacar(saldo=saldo, extrato=extrato)
                saldo = result[0]
                extrato = result [1]
                saques += 1

        elif opcao == 3:
            historico(saldo,extrato=extrato)

        elif opcao == 4:            
            print(f"saques realizados:{saques}")
        elif opcao ==5:
            criarCliente(clientes)
        elif opcao == 6:
            criarContaCorrente(AGENCIA, clientes, contas)
        elif opcao == 7:
            contasExistentes(contas)
       

    except ValueError: print("valor precisa ser um numero")