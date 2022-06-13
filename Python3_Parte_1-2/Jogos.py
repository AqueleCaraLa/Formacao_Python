import Forca
import Adivinhacao #importa o arquivo adivinhacao.py, para ser utilizado como módulo

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Adivinhação (2) Forca")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("\nJogando adivinhacao\n")
    Adivinhacao.jogar() #executa o arquivo selecionado (módulo.function())
elif (jogo == 2):
    print("\nJogando forca\n")
    Forca.jogar()