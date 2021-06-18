'''
exercicio: 
preencher um vetor com 100 numeros sorteados de 10 a 99 [10,99],
depois pergunta uma busca nesse vetor,
depois mostra se essa busca existe.

comandos e funções úteis:

- from random import randint

- randint(0, 2)

- for i in range(1, 11, 1):

- v2 = [0]*10
'''

from random import randint  #pra usar a biblioteca de valores randons/sorteados

v = [0]*100
for i in range(0, 100, 1):
    v[i] = randint(10,99)
print(v)

busca = int(input("Qual a chave de busca?: "))
qtde = 0

for i in range(0,100,1):
    if busca == v[i]:
        qtde = qtde + 1
        print(f'Encontrei o valor {busca} na posicao {i}')
print(f'Achei <{qtde}> ocorrências de {busca}')