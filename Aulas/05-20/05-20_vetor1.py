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