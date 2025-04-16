import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prazo):
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.concluida = False
        self.data_criacao = datetime.now().strftime('%d/%m/%Y')

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = '✅' if self.concluida else '⏳'
        return f'{status} {self.titulo} | Prazo: {self.prazo} | Criada em: {self.data_criacao}'


# Lista de tarefas
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    prazo = entry_prazo.get()

    if not titulo:
        messagebox.showwarning("Atenção", "O título da tarefa é obrigatório.")
        return

    nova = Tarefa(titulo, descricao, prazo)
    tarefas.append(nova)
    atualizar_lista()
    entry_titulo.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_prazo.delete(0, tk.END)

# Atualiza a lista de tarefas na interface
def atualizar_lista():
    lista.delete(0, tk.END)
    filtro = filtro_status.get()
    for tarefa in tarefas:
        if filtro == "Todas":
            lista.insert(tk.END, str(tarefa))
        elif filtro == "Pendentes" and not tarefa.concluida:
            lista.insert(tk.END, str(tarefa))
        elif filtro == "Concluídas" and tarefa.concluida:
            lista.insert(tk.END, str(tarefa))

# Marca a tarefa selecionada como concluída
def concluir_tarefa():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para concluir.")
        return
    index = selecao[0]
    tarefa_selecionada = filtrar_tarefas()[index]
    tarefa_selecionada.marcar_como_concluida()
    atualizar_lista()
    messagebox.showinfo("Sucesso", f"Tarefa '{tarefa_selecionada.titulo}' concluída!")

# Aplica o filtro na lista de tarefas
def filtrar_tarefas():
    filtro = filtro_status.get()
    if filtro == "Todas":
        return tarefas
    elif filtro == "Pendentes":
        return [t for t in tarefas if not t.concluida]
    elif filtro == "Concluídas":
        return [t for t in tarefas if t.concluida]

# Interface
app = tk.Tk()
app.title("✅ Gerenciador de Tarefas")
app.geometry("500x500")

tk.Label(app, text="Título:").pack()
entry_titulo = tk.Entry(app, width=50)
entry_titulo.pack()

tk.Label(app, text="Descrição:").pack()
entry_descricao = tk.Entry(app, width=50)
entry_descricao.pack()

tk.Label(app, text="Prazo (ex: 20/04/2025):").pack()
entry_prazo = tk.Entry(app, width=50)
entry_prazo.pack()

tk.Button(app, text="Adicionar Tarefa", command=adicionar_tarefa).pack(pady=5)

# Filtro
tk.Label(app, text="Filtrar tarefas por status:").pack()
filtro_status = ttk.Combobox(app, values=["Todas", "Pendentes", "Concluídas"])
filtro_status.current(0)
filtro_status.pack()
filtro_status.bind("<<ComboboxSelected>>", lambda event: atualizar_lista())

# Lista de tarefas
lista = tk.Listbox(app, width=80, height=10)
lista.pack(pady=10)

tk.Button(app, text="Concluir Tarefa Selecionada", command=concluir_tarefa).pack(pady=5)

app.mainloop()
