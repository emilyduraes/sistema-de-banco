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