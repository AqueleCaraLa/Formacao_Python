

class Conta: 
    
    def __init__(self, numero, titular, saldo, limite): # função contrutora no qual constroi o objeto / self é a referência que sabe encontrar o objeto que ta sendo construído
        print('Construindo objeto ... {}'.format(self))
        self.__numero = numero # o self. diz para a referencia(self) ir(.) ao objeto(numero) e acessar o atributo(numero)
        self.__titular = titular
        self.__saldo = saldo # encapsulamento de atributo, no qual só deve ser alterado usando os métodos
        self.__limite = limite # privatiza o atributo, no qual só pode ser acessado dentro da classe (conta._Conta__limite)

    def extrato(self):
        print('Saldo de {} do titular: {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor): # método para alterar o atributo do objeto
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # método privado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self): # o get nunca muda nada, somente retorna o valor
        return self.__limite

    @limite.setter
    def limite(self, limite): # o set irá mudar o valor
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    # set e get são nomenclaturas padrão para os métodos de 'mundança' e 'retorno'



    