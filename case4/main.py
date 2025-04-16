
from tarefa import Tarefa
from usuario import Usuario


def menu():
    print('\n--- MENU ---')
    print('1 - Adicionar tarefa')
    print('2 - Listar todas as tarefas')
    print('3 - Listar tarefas pendentes')
    print('4 - Listar tarefas concluídas')
    print('5 - Marcar tarefa como concluída')
    print('0 - Sair')

def main():
    nome = input('Digite o nome do usuário: ')
    usuario = Usuario(nome)

    while True:
        menu()
        opcao = input('Escolha uma opcão: ')

        if opcao == '1':
            titulo = input('Título da tarefa: ')
            descricao = input('Descrição: ')
            prazo = input('Prazo (dd/mm/aaaa): ')
            tarefa = Tarefa(titulo, descricao, prazo)
            usuario.adicionar_tarefa(tarefa)
            print('Tarefa adicionada com sucesso!')
        elif opcao == '2':
            print('\n--- Todas as Tarefas ---')
            usuario.listar_tarefas(tarefa)
        elif opcao == '3':
            print('\n--- Tarefas Pendentes ---')
            usuario.listar_tarefas(concluida=False)
        elif opcao == '4':
            print('\n--- Tarefas Concluídas ---')
            usuario.listar_tarefas(concluida=True)
        elif opcao == '5':
            titulo = input('Digite o título da tarefa a concluir: ')
            usuario.concluir_tarefa(titulo)
        elif opcao == '0':
            print('Saindo... Até a próxima!')
            break
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    main()
