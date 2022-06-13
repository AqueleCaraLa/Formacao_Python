class Programa:
    def __init__(self, nome, ano): #inicializador init, no qual será definido os atributos
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property # retono do atributo
    def likes(self):
        return self._likes

    def dar_like(self): # método para o objeto
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter # utilizado para se colocar um novo nome ao atribyto
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano}: {self.likes}'

class Filme(Programa): #utilização da herança class nome('classe mãe')
    def __init__(self, nome, ano, duracao): 
        super().__init__(nome, ano) #faz com que a classe receba os atributos da classe mãe
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min: {self.likes} Likes'


class Serie(Programa): #cria uma classe no qual será definido os métodos e atributos do objeto
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) 
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas: {self.likes} Likes'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160) # objeto que será criado, 'variavel' = 'Classe'(atributos)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')