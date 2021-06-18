import numpy as np #para dar um apelido e n ter que digitar numpy sempre
# www.numpy.org

#python padrão:
v = [1, 2, 3, 4]
#v.append(5) coloca 5 no final do vetor/da lista
print(v)
print(type(v))
print(type(v[0]))


vet = np.array(v) #criando vetor no numpy
#1 jeito de criar vetor no numpy é passando uma lista do python padrao

print(vet)
print(type(vet))
print(vet.dtype)
print(type(vet[0])) #tipo do elemento 1 da lista
print(vet.dtype.name)
print(vet.itemsize) #tamanho de cada elemento do vetor
print(vet.shape) #retorna dimensao, uma tupla
print(vet.ndim) #vetor de dimensao 1, unidimensional
print(vet.size) #tamanho do vetor inteiro, 4 elementos

m = [[1,2,3], [4, 5, 6]] 
print(m)
print(m[0])
print(m[0][1])
print(type(m)) #matriz = lista de listas

mat = np.array(m) #array específico para processamento matemático da biblioteca, q transforma a lista pro array do numpy
print(mat)
print(type(mat))
print(mat.shape) #dimensões do array, devolve uma tupla (2,3), q é uma matriz 2x3
print(mat.ndim) # numero de dimensões: 2, pois é bidimensional (2x3)
print(mat.size) #quantos elementos tem na matriz/lista

vp = list(range(1, 6, 1)) #vetor do python original, que cria e printa uma lista com valores separados por vírgula e n aceita passo float, só inteiro
print(vp)
vnp = np.arange(1, 6, 1) #vetor do numpy (vnp), range do numpy q substitui o do python= arange
print(vnp)
print(vnp.shape)

vnp2 = np.arange(0, 4.1, 0.5) # inicio, fim-, passo
#cria a lista com passo de 0.5, e vai até menos que 4.1 (4.0). O numpy tem essa precisão e possibilidade
print(vnp2)

vnp3 = np.linspace(0, 4, 20) #inicio, fim, qtde de elementos (fim fechado, conta até o número que colocou no linspace, no caso até o 4)
#nao fala o passo, fala quanto de elemento que quer
print(vnp3)

mnp = np.arange(15).reshape(3, 5) #arange cria lista com 15 elementos. Já o reshape = 3x5, dimensao que quer
print(mnp)
lp = list(range(200)) #lista padrao python sem os valores default, sem o 0 q é o inicio, sem o passo (1 é o default), e usando só o 200 que é qtde de elementos
print(lp)

mnp2 = np.array(lp).reshape(5, 40) #reshape cria a matriz com o array e atribui a mnp2, q é a matriz em numpy com o comando do numpy reshape
print(mnp2)

mnp3 = np.zeros((3, 3)) #cria matriz no numpy de dim 3x3 preenchida de zeros
print(mnp3)
print(mnp3.shape) #(3,3)
print(mnp3.dtype.name) # dtype.name nesse caso = float 64 bits

mnp4 = np.ones((3, 2, 6), dtype=np.int16) #matriz tridimensional preenchida de um's, 3x2x6, 3 faces de 2 linhas e 6 colunas
print(mnp4)
print(mnp4.dtype.name)

mnp5 = np.empty((4, 8), dtype=np.int64) #preenchida com sujeira de memória, valores qualquer = empty
print(mnp5)
print(mnp5.dtype.name)