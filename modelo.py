class Programa:
    def __init__(self, nome, Ano):
        self.__nome = nome.title()
        self.Ano = Ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter 
    def nome (self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

class Filme(Programa):
    def __init__(self, nome, Ano):
        self.__nome = nome.title()
        self.Ano = Ano
        self.__likes = 0

class Serie(Programa):
    def __init__(self, nome, Ano, temporadas):
        self.__nome = nome.title()
        self.Ano = Ano
        self.temporadas = temporadas
        self.__likes = 0

  
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'nome: {vingadores.nome} - Ano: {vingadores.Ano} - duraçao: {vingadores.duraçao} - likes: {vingadores.likes}')

atlanta =Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'nome: {atlanta.nome} - Ano: {atlanta.Ano} - temporadas: {atlanta.temporadas} - likes: {atlanta.likes}')
