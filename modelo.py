class Filme:
    def __init__(self, nome, Ano, duraçao):
        self.nome = nome.title()
        self.Ano = Ano
        self.duraçao = duraçao
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, Ano, temporadas):
        self.nome = nome.title()
        self.Ano = Ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'nome: {vingadores.nome} - Ano: {vingadores.Ano} - duraçao: {vingadores.duraçao} - likes: {vingadores.likes}')

atlanta =Serie('atlanta', 2018, 2)
print(f'nome: {atlanta.nome} - Ano: {atlanta.Ano} - temporadas: {atlanta.temporadas} - likes: {atlanta.likes}')
