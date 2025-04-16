from datetime import datetime


class Tarefa:
    def __init__(self, titulo, descricao, prazo):
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.concluida = False
        self.data_descricao = datetime.now().strftime('%d/%m/%Y')

    def marcar_como_concluida(self):
        self.concluida = True
    
    def __str__(self):
        status = '✅' if self.concluida else '⏳'
        return f'{status} {self.titulo} | Prazo: {self.prazo} | Criada em: {self.data_descricao}'
