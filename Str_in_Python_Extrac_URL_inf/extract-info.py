#url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar' # parte da url em formato de string

url = ''

# Sanitização da URL para
url = url.replace(' ', '')

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia')


#separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(url_base)
print(url_parametros)
print(valor)
