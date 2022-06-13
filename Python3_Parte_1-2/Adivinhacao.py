import random #parecido com uma biblioteca, o import, importa a biblioteca para podermos usar suas funções

def jogar(): #define o arquivo, assim pode ser usado em outro arquivo

    print('************************************')
    print('Bem vindo ao jogo de Adivinhação!!!!')
    print('************************************\n')

    #variáveis
    #numero_secreto = 45 
    total_de_tentativas = 0
    rodada = 1
    numero_secreto = round(random.random()*100) #gera números aleatórios até 100 no formato float. Função round arredonda o número float
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil\n')

    nivel = int(input('Define o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # while(rodada <= total_de_tentativas): 
    # utilizando o while, enquanto a condição em parenteses for verdadeira, repete o bloco abaixo

    for rodada in range(1, total_de_tentativas + 1):
        # o for é uma função no qual incrementa até certo valor, utilizando o range temos (inicio, fim(n-1), opcional: pula os valores). O for é utilziado como alternativa para o while; 
        
        print('\nTentativa {} de {}'.format(rodada, total_de_tentativas)) 
        # imprime o número de tentativas que o jogador possui, o .format é uma função que joga os valores das variáveis dentro do {}
        
        chute_str = input('Digite um número entre 1 e 100: ') 
        # A função input recebe o que a pessoa escreve e devolve em formato de string

        print('Você digitou', chute_str)
        chute = int(chute_str) # Transforma a string do input em um inteiro

        if(chute < 1 or chute > 100): #or é utilizado para duas condições diferentes
            print('Você deve digitar um número entre 1 e 100!')
            continue #sai da interação e continua para a próxima rodada
        
        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou): 
            # A função if e else são usadas para caso tenha dois tipos de condições que podem ocorrer, precisam de dois ponto no final
            print('Você acertou e fez {} pontos\n'.format(pontos))
            break
        else:
            if(chute_maior): 
                print('Você errou! O seu chute foi maior do que o número secreto.\n')
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            elif(chute_menor): # A função elif é usada da mesma forma que o if ou o else
                print('Você errou! O seu chute foi menor do que o número secreto.\n')
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            
            pontos_perdidos = abs(numero_secreto - chute) #a função abs faz com que o resultado da conta seja seu módulo
            pontos = pontos - pontos_perdidos
        #rodada = rodada + 1 
        # aumenta o número de rodadas que o jogador jogou
    print('Fim do jogo!\n')

if(__name__ == '__main__'): #utlizado para que o arquivo seja executado em adivinhacao.py e jogos.py
    jogar()