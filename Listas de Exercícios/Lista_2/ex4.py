import numpy as np
from numpy.core.fromnumeric import size

'''
4) Crie uma função python que retorna o maior de dois números enviado por parâmetro.
   Ela irá funcionar de maneira regular, ou seja, operando sobre 2 escalares.
   Verifique o funcionamento da função NumPy vectorize, e crie então a função
   que opera sobre vetores.
   Teste sua função com dois arrays numpy de 10 posições sorteadas de números inteiros
   no intervalo [10, 100) (usando funções NumPy).
   Mostre os 3 vetores.
'''

def Maior(a, b):

    if a > b:
        return a
    else:
        return b

Maior_comp = np.vectorize(Maior) # Maior_comp é a função que vai permitir a manipulação dos 2 vetores
vect_a = np.random.randint(10, 100, size = (1,10)) # [low, high) = 100 excluso
print("1º vetor: ", vect_a)
vect_b = np.random.randint(10, 100, size = (1,10))
print("2º vetor: ", vect_b)

vect_res = Maior_comp(vect_a, vect_b)
print("vetor resultado: ", vect_res)
print()