# Vetor em C:
# int v1[] = {1,2,3};
# int v2[10] = {0};

# Python não tem um 'tipo array' para vetor e matriz
# usa-se listas:

'''
v1 = [1,2,3]
print(v1)
print(len(v1)) #len = length, comprimento
print(type(v1))

v1[0] #índices
v1[0] = 5 #mudando o valor do índice
print(v1)

v1[-1] = 8 #mudando o último valor da lista, usando índice negativo pra começar do fim
print(v1)

v1.append(1)
v1.append(9) #transforma num vetor maior, adicionando os valores na frente
print(v1)

v1.reverse() #inverte a ordem
print(v1)

v1.sort() #ordena por ordem crescente
print(v1)
'''
'''
v2 = [] #lista vazia
print(len(v2)) #depois, fazer um loop com 10 appends pra preencher, caso use essa sintaxe

v2 = [0]*10 #mas tem essa opcao
print(len(v2))
print(v2)
'''


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