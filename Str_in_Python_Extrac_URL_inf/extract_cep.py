endereco = 'Rua Jorge Feliciano da Silva 35, Monte Belo, Londrina, PR, 86041-610'

import re #regular Expression -- ReqEx

# 5 digitos + hífen (opcional) + 3 digitos (padrão a ser encontrado)

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}') # criação de padrão a ser descoberto, o '?' diz que o valor anterior é opcional
busca = padrao.search(endereco) # objeto Match, no qual retorna o valor caso encontre o padrão e NONE caso não encontre o padrão

if busca:
    cep = busca.group() # agrupa o padrão e o referencia em uma variavel
    print(cep)

