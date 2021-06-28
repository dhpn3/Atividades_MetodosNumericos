'''
4) Plote a curva dada por:
   x = sen t
   y = 2 sen 4t
   Com t no intervalo [0, 2PI] com 100 pontos.
'''

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100) # intervalo do eixo t
x, y = np.sin(t), 2*np.sin(4*t)
plt.plot(t, x, ls = '--', color = 'brown')  # primeiro plot
plt.plot(t, y, ls = '--', color = 'b')  # segundo plot
plt.show()  # mostra na tela todos os plots feitos