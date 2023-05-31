saldo = 100
qttd_saques = 0
transacoes = []

def deposito():
    global saldo
    valor = float(input('qual valor deseja depositar?: '))

    if valor > 0:
        saldo += valor
        extrato('Deposito', valor)

    else:
        return ('não é possivel depositar valores negativos')
    return(f'''Seu deposito foi realizado com sucesso seu saldo é de {saldo:.2f}''' )


def saque():
    global saldo, qttd_saques
    valor = float(input('Por gentileza, informe o valor que gostaria sacar?: '))

    if valor < saldo and qttd_saques < 3 and valor < 500 :
        saldo -= valor
        extrato('Saque',valor)
        qttd_saques += 1
    elif valor > saldo:
        return "Não tem saldo o suficiente"
    else:
        return "Não foi possivel realizar seu Saque"
        
    return "Saque realizado com sucesso"

    
def extrato(tipo, valor):

    if tipo == 'Saque':
        negativo = valor * -1
        transacoes.append([tipo,negativo])
    else:
        transacoes.append([tipo,valor])

def imprimir_extrato():
    print(transacoes)
    print(f'seu saldo é R${saldo:.2f}',)

while True:

    print(''' 
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair

    ''')

    opcao = int(input('por gentileza escolhar uma opção: '))

    if opcao == 1:
        print(deposito())
    elif opcao == 2:
        print(saque())
    elif opcao == 3:
        imprimir_extrato()
    elif opcao == 4:
        print('Obrigado por ser nosso cliente')
        break
    else:
        print('Opção invalida!!')
