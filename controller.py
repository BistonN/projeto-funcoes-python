import os

def login(usuarios:list):
    n_conta = input('Digite o numero da conta: ')
    usuario_encontado = {}
    for usuario in usuarios:
        if usuario['n_conta'] == n_conta:
            usuario_encontado = usuario 

    if not usuario_encontado:
        os.system('clear')
        print(f'Numero da conta {n_conta} não encontrado!')
        return

    senha = input('Digite a senha da conta: ')

    if senha == usuario_encontado['senha']:
        print(f'Seja bem vindo {usuario_encontado["nome"]} ')
        home(usuario_encontado) 
    else:
        os.system('clear')
        print('Senha da conta incorreta!')
        return

def parse_float(numero_string):
    return float(numero_string.replace(',', '.'))
    
def home(usuario:dict): 
    escolha = input(
'''
Digite (1) para ver Saldo
Digite (2) para Depositar
Digite (3) para Sacar
Digite (4) para Logoff
'''
    )
    if escolha == '1':
        os.system('clear')
        print(f'Saldo Atual: {usuario["saldo"]}')
        home(usuario)
    elif escolha == '2':
        try:
            deposito = parse_float(input('Valor do deposito: '))
            usuario["saldo"] += deposito
            home(usuario)
        except:
            os.system('clear')
            print('Digite um valor válido para deposito!')
            home(usuario)
    elif escolha == '3':
        pass
    elif escolha == '4':
        print('Logoff...')
        return



