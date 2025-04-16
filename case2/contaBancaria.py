class ContaBancaria:

    def __init__(self):
        self.saldo = 0


    def depositar(self, valor):
        if valor <= 0:
            print('Valor invalido. O depósito precisa ser maior que zero')
        else:
            self.saldo += valor
            print(f'Saldo: {self.saldo}')
    

    def sacar(self, valor):

        if(valor > self.saldo):
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saldo: {self.saldo}')
    
    def verSaldo(self):
        print(f'Saldo: {self.saldo}')