'''
Escreva um algoritmo que jogue Joquempô (Pedra, Papel e Tesoura) com o usuário; o programa escolhe
randomicamente a jogada do computador, depois lê a opção do usuário e finalmente mostra o
resultado da rodada: vitória do computador, vitória do usuário ou empate.
'''
from random import randint
comp = randint(1, 3) # sorteia no intervalo [1..3]
print(comp)
user = int(input("1 - Pedra, 2 - Papel, 3 - Tesoura, opção? "))
# cobrir vitoria comp e cobrir vitoria do user
# terminarem... if, elif, else ?

# estes QUATRO formatos de validar a entrado do usuário são equivalentes
#if user not in [1, 2, 3]:
#if user!=1 and user!=2 and user!=3:
#if user>3 or user<1:
if user not in range(1, 4, 1): # formato do range(inicio, final, incremento)
    print("Você digitou um valor incorreto!")
elif user == comp: # resolve para as 3 possibilidade de empate
    print("Empate")
elif user == 1: # sabe-se que comp não foi 1
    if comp == 2:
        print("Papel embrulha pedra, computador ganhou!")
    else: # não é 1 e não é 2, sobrou 3
        print("Tesoura não corta pedra, usuário ganhou!")
elif user == 2: # sabe-se que comp não foi 2
    if comp == 1:
        print("Papel embrulha pedra, usuario ganhou!")
    else: # não é 1 e não é 2, sobrou 3
        print("Tesoura corta papel, computador ganhou!")
else: # sobrou apenas 3, sabe-se que comp não foi 3
    if comp == 1:
        print("Tesoura não corta pedra, computador ganhou!")
    else: # não é 1 e não é 3, sobrou 2
        print("Tesoura corta papel, usuario ganhou!")