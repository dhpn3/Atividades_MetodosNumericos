# aula está gravada no teams
import numpy as np
from scipy import linalg #algebra linear

# resolver o sistema linear de equações com a função a biblioteca linealg 'solve'
# 3x1  +  x2 = 0
#  x1  + 2x2 = 8

a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = linalg.solve(a, b)
print(x) # devolve o valor de x1=2 e x2=3 
print("Valor de x1: ", x[0]) # x1 = 2
print("Valor de x2: ", x[1]) # x2 = 3
print()