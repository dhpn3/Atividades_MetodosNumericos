import numpy as np

'''
3) Usando NumPy, crie uma matriz mA 5x5 com numeros aleatórios no intervalo [1, 9].
   (use np.random.randint ou crie gerador com np.random.default_rng() e use o método integers,
   ver ambas opções na documentação).
   Inicialize uma matriz identidade mId 5x5 e teste a função de multiplicação de matrizes (@ ou dot)
   entre mA e MId. Faça também a transposta (transpose ou T) de mA e a inversa (I) de mA.
   Pesquise como calcular o determinante de mA (módulo linalg do numpy), mostrando o valor do determinante.
'''

# fontes:

# https://www.delftstack.com/pt/api/numpy/python-numpy-linalg.inverse/
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# http://pyscience-brasil.wikidot.com/docitem:numpy-identity

mA= np.random.randint(5, size = (5, 5)) #matriz A 5x5 randômica
print('mA randômica: \n', mA)
print()

mId = np.identity(5, dtype=int) #função da biblioteca Numpy que pesquisei pra não ter que digitar todo o array
print('identidade: \n', mId)
print()

mm = mA @ mId
print('mA x identidade:\n', mm) # mm == mA: a multiplicação duma matriz por uma identidade resulta nela mesma.
print()

mT = mA.transpose() #transposta da mA
print('matriz transposta de mA: \n', mT)
print()

mInv = np.linalg.inv(mA)
print('matriz inversa de mA: \n', mInv)
print()

det = np.linalg.det(mA)
print('determinante: \n', round(det, 3))
print()