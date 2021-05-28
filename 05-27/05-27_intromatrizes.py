# usando list para array do tipo vetor - 1 dimensão
vetor = [1,2,3,4]

#usando list para array do tipo matriz - 2 dimensões, (3x3)
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print("Matriz inteira: ", matriz)
print("Matriz linha 0: ", matriz[0])
print("Matriz posicao 0,2: ", matriz[0][2])

for i in range(3):  #laço para printar ela no formato matricial
    for j in range(3):
        print(matriz[i][j], end = "  ")
    print() #print vazio pula linha


m = [[1,2], [3,4,5], [6,7,8,9]] #matriz anômola/não quadrada

for i in range(len(m)): # este len() da matriz retorna o total de linhas
    for j in range(len(m[i])): # e este len() da matriz retorna o total de colunas da linha 'i'
        print(m[i][j], end = "  ")
    print() #print vazio pula linha


#exercicio de multiplicacao de matrizes para 10/06

#perguntar linha L e coluna C da matriz A
#perguntar linha L e coluna C da matriz B
# se pode multiplicar, faz a operação, resulta matriz resultado MatR

#criar uma matriz 3x10 (exemplo)

'''
mat = [0]*3 # 3 linhas, [0]*lA pro exercício
for i in range(10):
    mat[i] = [0]*10 #criando as 10 colunas, [0]*lB
'''