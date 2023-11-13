## sistema de caixa de banco
## acesso a conta, criarção de uma conta, ver o saldo, 
## sacar, depositar
import os
import controller as ctl

usuarios = [
    {'nome': 'Usuario1', 'n_conta': '1234', 'saldo': 2500.0, 'senha': '1234' },
    {'nome': 'Usuario2', 'n_conta': '5678', 'saldo': 1500.0, 'senha': '5678' },
    {'nome': 'Usuario3', 'n_conta': '9101', 'saldo': 6500.0, 'senha': '9101' },
    {'nome': 'Usuario4', 'n_conta': '1213', 'saldo': 100.0, 'senha': '1213' }
]

while (True):
    escolha = input('''
Digite (1) para Login
Digite (2) para Sair
''')
    if escolha == '1':
        os.system('clear')
        ctl.login(usuarios)
    elif escolha == '2':
        print('Saindo...')
        break
    else:
        os.system('clear')
        print('Digite uma opção válida')