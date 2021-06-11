from random import randint
opcoes = ["Pedra", "Papel", "Tesoura"]
comp = randint(0, 2) # sorteio no intervalo [0, 2]
humano = int(input("0-Pedra, 1-Papel, 2-Tesoura: "))
print("Humano jogou:", opcoes[humano])
print("Computador jogou:", opcoes[comp])

if comp == humano:
    print("Empate!")
elif humano == 0 and comp == 2 or \
     humano == 1 and comp == 0 or \
     humano == 2 and comp == 1:
    print("Humano ganhou!!!")
else:
    print("Computador ganhou!!!")


# operadores relacionais devolvem valor True ou False
# >   >=  <   <=   ==  !=

# python aceita:   -10 <= x <= 10
# em C: ((-10<=x) && (x <= 10))

# operadores lógicos  operam logicamente
#  and   or   not