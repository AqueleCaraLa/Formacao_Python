
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property # diz que o método representa uma propriedade, não precisa dos parenteses
    def nome(self):
        print('chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('chamando setter nome()')
        self.__nome = nome