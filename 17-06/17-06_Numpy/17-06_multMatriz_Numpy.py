import numpy as np

ma = np.array([[1, 2], [3, 4]]) #matriz a
mi = np.array([[1, 0], [0, 1]]) #matriz identidade
print(ma)
print(mi)
msoma = ma + mi #soma matricial, soma as células corretas e colocam nos lugares corretos
print()
print(msoma)

mmult = ma * 3 # multiplicacao escalar
print()
print(mmult)

mm = ma @ mi #multiplicao matricial (matriz vezes matriz)
#pode ser feito tb como: mm = ma.dot(mi), q é o produto entre 2 arrays
# ma @ mi é equivalente a ma.dot(mi)
print()
print(mm)

mt = mmult.transpose() #matriz transposta, inverte a diagonal
print(mt)
print(mt.sum()) #soma dos valores
print(mt.max()) #maior valor 
print(mt.min()) #menor valor

# e assim por diante, continua na documentação