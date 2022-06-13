#---------------------------------------------------------------------------------
idades = [60, 50, 25, 20]
print(type(idades))
print(len(idades))
print(idades[0])
print(idades)
idades.append(10)
print(idades, '\n')

for idade in idades:
    print(idade)

idades.remove(20)
print(idades)

idades.clear()
print(idades)

#--===============================================================================

idades = [60, 50, 25, 20]

a = 55 in idades
b = 60 in idades
print(a, b)

if 60 in idades:
    idades.remove(60)
print(idades)

if 60 not in idades:
    idades.insert(0, 60)
print(idades)

idades.append([33, 66])
print(idades)
for elemento in idades:
    print('Recebi o elemento', elemento)

idades.remove([33, 66])
print(idades)

idades.extend([33, 66])
print(idades)
idades.remove(33)
idades.remove(66)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

idades_em_dois_anos = [(idade+2)for idade in idades]
print(idades_em_dois_anos)

filtro = [(idade)for idade in idades if idade > 25] 
print(filtro)

def proximo_ano(idade):
    return idade + 1

metodo = [proximo_ano(idade) for idade in idades if idade > 24]
print(metodo, '\n')

#======================================================================

def faz_processamento_de_visualizacao(lista):
    lista.append(13)
    print(len(lista))

process = faz_processamento_de_visualizacao(idades)
print(idades)

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
    print(lista)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

#---------------------------------------------------------------------------

