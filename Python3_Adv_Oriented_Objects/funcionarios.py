class Funcionario: #classe mãe
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas): # método
        print('Horas registradas...')

    def mostrar_tarefas(self): #método
        print('Fez muita coisa...')

class Caelum(Funcionario): #classe filha no qual recebe os métodos e atributos da classe mãe
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostra cursos desse mês')

class Alura(Funcionario): #classe filha no qual recebe os métodos e atributos da classe mãe
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self): #método
        print('Monstrando perguntas não respondidas do fórum')

class Hipster: #Mixin no qual retorna um método que pode ser utilizado por outras classes
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)