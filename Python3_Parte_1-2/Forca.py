import random

def jogar():

    imprime_mensagem_abertura() # faz com que seja imprimido a função no qual foi definida
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) 
    print(letras_acertadas)

    enforcou = False
    acertou = False # variavel booleanos
    erros = 0

    while(not enforcou and not acertou): #enquanto (not 'False' and not 'False') = enquanto(True and True) 
        
        chute = pede_chute()
       
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1 
            desenha_forca(erros)

        enforcou = erros == 7

        acertou = '_' not in letras_acertadas # acertou continuara FALSE enquanto tiver '_' em letras_acertadas
        print(letras_acertadas) #imprime a lista

    if(acertou):
        imprime_mensagem_vencedor()
    else: 
        imprime_mensagem_perdedor(palavra_secreta)
 
def imprime_mensagem_abertura():
    print('************************************')
    print('**** Bem vindo ao jogo da Forca! ***')
    print('************************************\n')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r') #abre o arquivo .txt no qual estará no modo de leitura 'r'
    palavras = [] # lista no qual ficara a palavra

    for linha in arquivo: #faz a leitura de uma linha de cada vez
        linha = linha.strip()
        palavras.append(linha) 

    arquivo.close() #fecha o arquivo

    numero = random.randrange(0, len(palavras)) # variavel no qual selecionara uma posição aleatória do arquivo aleatória
    palavra_secreta = palavras[numero].upper() # colocara o numero em palavra
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]  # Cria uma lista de strings no qual poderá ser trocado pelas letras do chute
    #abaixo ou forma de se fazer a incrementação da lista de acordo com palavra_secreta
    #for letras in palavra_secreta:
    #    letras_acertadas.append() 

def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper() #Função .strip() remove os espaçoes em branco #Função .upper() faz com que todas as letras fiquem maiusculas
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0 #posição
    for letra in palavra_secreta: 
        if(chute == letra): #mostra somente as letras que são iguais ao chute
            letras_acertadas[index] = letra  #faz com que a lista receba a posição(index) da letra do chute
        index += 1 #incrementa em 1 de acordo com a posição da letra (index = index + 1)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == '__main__'):
    jogar()

