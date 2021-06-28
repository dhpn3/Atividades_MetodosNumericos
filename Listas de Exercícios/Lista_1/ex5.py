'''
5) Plote o polinômio:
   f(x) = 4xˆ5 -12xˆ3 -6x^2 -x -2
   Com x no intervalo [-2, 2] com 200 pontos. 
   Coloque o f(x) em uma função: 
   def f(x): 
      # retorno da equação
   Antes de plt.show(), chame plt.grid().
'''

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**5 -12*x**3 -6*x**2 -x -2

x = np.linspace(-2, 2, 200)
plt.plot(x, f(x))
plt.grid()
plt.show()