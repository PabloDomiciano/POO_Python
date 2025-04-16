class Pessoa ():
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade

    def apresentar(self):
        return print(f'Ola, meu nome é {self.nome} e tenho {self.idade} anos')