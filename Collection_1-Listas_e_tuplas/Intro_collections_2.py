class ContaCorrente:
    def __init__(self, codigo): 
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self.codigo, self.saldo)

conta_1 = ContaCorrente(15)
conta_1.deposita(10)
print(conta_1)

conta_2 = ContaCorrente(5508)
conta_2.deposita(1000)
print(conta_2)

contas = [conta_1, conta_2] #colocar objetos na lista, não instancia um objeto novo.
print(contas)

for conta in contas:
    print(conta)

contas[1].deposita(1000)
print(conta_2, '\n')

#================================================================================================

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(2000)

contass = [conta_1, conta_2]
print(contass[0], contass[1])
deposita_para_todas(contas)
print(contass[0], contass[1])

contass.insert(0, 77)
print(contass[0], contass[1], contass[2])

igor = ('Igor', 20, 2002) # tupla
conta_igor = (20, 1000)

def deposita(conta): #variação 'funcional' (separando o comportamento de dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)
    
deposita(conta_igor)
nova_conta_igor = deposita(conta_igor)
print(nova_conta_igor, '\n')

#================================================================================================

igor = ('Igor', 20, 2002)
eliza = ('Eliza', 40, 1982)
usuarios = [igor, eliza]
print(usuarios)
usuarios.append(('Pedro', 23, 1999))
print(usuarios)

conta_3 = ContaCorrente(13)
conta_3.deposita(600)
conta_4 = ContaCorrente(25)
conta_4.deposita(1000)

contas = (conta_3, conta_4)

for conta in contas:
    print(conta)

contas[0].deposita(600)
for conta in contas:
    print(conta)