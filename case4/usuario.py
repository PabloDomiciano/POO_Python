class Usuario():
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self, concluida=None):
        for tarefa in self.tarefas:
            if concluida is None or tarefa.concluida == concluida:
                print(tarefa)
    
    def concluir_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.marcar_como_concluida()
                print(f'Tarefa: {titulo}, marcada como concluída')
                return
        print('Tarefa não encontrada') 