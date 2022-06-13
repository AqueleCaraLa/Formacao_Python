################## LISTAS ###########################

lista = [2, 5, 6, 7, 8, 20, 0, 11, 12, 13]
palavra = 'banana' 
# ambos são listas

funcao_len = len(palavra) #mostra o número de valores dentro da lista
print(funcao_len)

funcao_min = min(lista) # mostra o menor valor dentro da lista
print(funcao_min)

funcao_max = max(lista) # mostra o maior valor dentro da lista
print(funcao_max)

funcao_index = palavra[3] # mostra o número na posição (0, 1, 2, 3, ...)
print(funcao_index)

funcao_append = lista.append(24) # adiciona o valor 24 na ultima posicao
print(lista)

funcao_pop = lista.pop() # a funcao pop retira o ultimo elemento
print(lista)

################## RANGE ###########################

serie = range(0, 10) # o segundo parametro é exclusivo, ou seja, não é aplicado

function_index = serie[9]
print(function_index)

################## TUPLE ###########################
# O Tuple é uma lista na qual não pode ser alteradas

dias = ('S', 'T', ' Q', 'Q', 'S', 'S', 'D') #a função tuple é utilizado quando colocamos parenteses ao inves de colchetes.
funcion_type = type(dias) #type mostra o tipo da variavel
print(funcion_type) 

#podemos utilizar as mesma funções que utilizamos nos outros tipos de sequencia, exceto pelas funções .pop() e .append()

p1 = (3, 5) #pontos de um gráfico, no qual são do tipo tupla
p2 = (4, 6)
p3 = (5, 7)

line = [p1, p2, p3] #os pontos são alocados para dentro de uma lista

print(line)

Pessoa1 = ('Igor', 19)
Pessoa2 = ('Vilson', 60)
Pessoa3 = ('Cida', 50)
Pessoa4 = ('Vinicius', 24)

lista_pessoas = [Pessoa1, Pessoa2, Pessoa3, Pessoa4]
print(lista_pessoas) #imprime a lista na qual está guardado os tuple 

print(lista_pessoas[0]) #imprime somente o primeiro conjunto dentro da lista ('Igor', 19)
print(lista_pessoas[0][1]) #imprime somente o primeiro conjunto e segundo valor do mesmo (19)

############### Descobrindo a idade pelo nome ############################

lista_pess = {'Igor' : 19, 'Vilson' : 60, 'Cida' : 50, 'Vinicius' : 24}

print(lista_pess['Vinicius'])

############### Convertendo Lista para Tuple #################################################
palavras = [] 
palavras.append('Banana')
palavras.append('Abacaxi')
print(palavras)

nova = tuple(palavras) # a função tuple() converte uma lista em tuple
print(nova)

outra = list(nova) # inversamente a função list() converte um tuple em uma lista
print(outra)

################ SET - REVER ############################

# SET é um diferente de uma sequencia pois não possui indice, não se pode ter valores duplicados. Ele é inicializado utilizando chaves {}

colecao = {160902, 271260, 270871, 180497}
print(colecao)

novo = colecao.add(200907)
print(colecao)

duplicado = colecao.add(160902) 
print(colecao)

# Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.