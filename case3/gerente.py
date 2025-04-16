from funcionario import Funcionario
from vendedor import Vendedor


class Gerente(Funcionario):
    def __init__(self, nome, vendas_proprias, vendedores=[]):
        super().__init__(nome)
        self.vendas_proprias = vendas_proprias
        self.vendedores = vendedores

    def calcular_pagamento(self):
        salario_fixo = 2000
        comissao_propria = (self.vendas_proprias * 5) / 100
        comissao_vendedores = sum([v.pegar_venda() for v in self.vendedores]) * 0.05 
        pagamento_total = salario_fixo + comissao_propria + comissao_vendedores
        return super().calcular_pagamento(pagamento_total)