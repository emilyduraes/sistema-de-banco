from random import randint

class Conta_bancaria():
    def __init__(self, titular, cpf, conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.conta = conta
        self.saldo = saldo

    def validar_usuário(self, titular, cpf):
        titular = input('Qual seu nome?')
        cpf = input('Qual seu CPF?')

class Banco():
    def __init__(self):
        conta_bancaria = {
            'Titular': titular,
            'CPF': cpf,
            'Número da Conta': conta,
            'Saldo': saldo
        }

    def criar_conta(self, conta, saldo):
        conta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        saldo = 0

        for conta in conta_bancaria:
            print(str(randint(0, len(conta)-1))+str(randint(0, len(conta)-1))+str(randint(0, len(conta)-1))+"-"+str(randint(0, len(conta)-1)))
            
    def depositar(self, saldo, valor):
        valor = input ('Digite o valor do depósito:')
        self.saldo += valor
        print(f'Seu novo saldo é de R$ {self.saldo}.')
    
    def sacar(self, saldo, valor):
        valor = input('Digite o valor do saque:')
        self.saldo -= valor
        print(f'Seu novo saldo é de R$ {self.saldo}.')

    def consultar_saldo(self, saldo):
        print(f'Olá, {self.titular}. Seu saldo atual é {self.saldo}.')
    
class Opcoes():
    self.banco = Banco()

    opcoes = input('Escolha uma ação e digite seu número: 1 - Consultar Saldo / 2 - Depositar / 3 - Sacar')
    
    if(opcoes == '1'): 
        print (self.banco.consultar_saldo())

    elif(opcoes ==  '2'):
        print (self.banco.depositar())

    elif(opcoes == '3'):
        print (self.banco.sacar())

    else:
        print('Digite apenas os valores numéricos citados.')


class Sistema():
    def __init__(self):  
        validar_usuário()
        opcoes()
    



#  conta:
#        atributos: titular, CPF, número e saldo
# banco:
#        atributos: contas
#        métodos: saque, depósito, consulta de saldo, criar conta (novo usuário), validar usuário
# interface:
#        atributos:  bancos

# ---------------------------------------------------------

# 1. O sistema permite que o cliente se cadastre:
#   "Digite seu nome:" input
#   "Digite seu cpf:" input

# 2. O sistema cria uma conta automaticamente para o cliente
#   "Olá João, sua conta é 1234-1" *fun aleatório *
# if criar_conta = contaCadastrada
# return contaCadastrada
# else 
# return criar_conta()

# 3. Após a criação da conta, o sistema exibe um menu: input + (fun 1 2 3)
#   "1- Consultar saldo"
#   "2- Depositar"
#   "3- Sacar"
# *if *
# Caso o cliente escolha a opção 1:
#   "Seu saldo é R$ 0" *print *
# Caso o cliente escolha a opção 2:
#   "Digite o valor: " input
#   "Depósito efetuado. Seu novo saldo é R$ 500" *print saldo+depósito *
# Caso o cliente escolha a opção 3:
#   "Digite o valor: " *input *
#   "Saque efetuado. Seu novo saldo é R$ 100" print saldo - saque
# Caso o cliente escolha a opção 3 e o saldo seja insuficiente: *else if saldo insuficiente *
#   "Digite o valor: " *input *
#   "Saldo insuficiente" *print *