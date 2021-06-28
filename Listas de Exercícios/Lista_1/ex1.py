'''
1) Utilizando sen, cos e linspace do NumPy mais matplotlib, calcule e apresente o gráfico
de sen(x) e de cos(x) no intervalo [-PI, +PI] no mesmo plot (pegando PI do NumPy). 
Use plot e show de forma básica.
'''

import matplotlib.pyplot as plt
import numpy as np

eixoX = np.linspace(-np.pi, np.pi, 100) # 100 valores 
Seno, Cos = np.sin(eixoX), np.cos(eixoX) # atribuição pro seno e cosseno
plt.title('Sen(x) e Cos(x)')
plt.xlabel('-π ≤ x ≤ π')
plt.ylabel('f(x) e g(x)')
plt.plot(eixoX, Seno)
plt.plot(eixoX, Cos)
plt.show()