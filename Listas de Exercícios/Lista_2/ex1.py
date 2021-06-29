'''
1) Plote os dois polinômios f(x) e g(x):
   f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18
   g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24
   Com x no intervalo [-4.5, 4.5] com 300 pontos. Antes de plt.show(), chame plt.grid(). 
   Implemente as funções em código Python:
   def f(x): 
      # retorno da função f
   def g(x): 
      # retorno da função g     
   Coloque as equações dos polinômios como rótulos (ver exemplo 7).
'''

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -2*x**4 + 3*x**3 + 7*x**2 -10*x +18

def g(x):
    return x**4 +2*x**3 -13*x**2 -14*x +24

x = np.linspace(-4.5, 4.5, 300)
plt.plot(x, f(x), color = 'r', label='f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18')
plt.plot(x, g(x), color = 'b', label='g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24')
plt.grid()  # rede na camada de trás
plt.legend()    # para acionar os rótulos cria-se uma legenda
plt.xlabel('x')
plt.ylabel('f(x) e g(x)')
plt.title('Polinômios')
plt.show()