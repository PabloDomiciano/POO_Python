from funcionario import Funcionario


class Vendedor(Funcionario):
    def __init__(self, nome, quantidade_venda):
        super().__init__(nome)
        self.quantidade_venda = quantidade_venda

    def calcular_pagamento(self):
        salario_fixo = 1500
        comissao = (self.quantidade_venda * 5) / 100
        pagamento_total = salario_fixo + comissao
        return super().calcular_pagamento(pagamento_total)
    
    def pegar_venda(self):
        return self.quantidade_venda