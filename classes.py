from random import randint

class Conta_bancaria():
    def __init__(self, titular, cpf, numero, saldo):
        self.titular = titular
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo    

class Banco():
    def __init__(self):
        self.contas = []

            for conta in contas:

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

    def criar_conta(self, titular, cpf):
        
        for conta in Contas:
           self.conta = randint(0, len(self.cartas)-1)
           saldo = 0

    def consultar_saldo(self, saldo):
        print(f'Olá, {self.titular}. Seu saldo atual é {self.saldo}')
    



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