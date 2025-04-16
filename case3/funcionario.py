from datetime import datetime

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.data_criacao = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    def calcular_pagamento(self, pagamento_minimo):
        print(f'{self.nome} Pagamento de: {pagamento_minimo:.2f}')
        print(f'Data de contratação: {self.data_criacao}')
