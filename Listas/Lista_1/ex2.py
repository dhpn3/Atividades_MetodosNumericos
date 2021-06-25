'''
2) Utilizando o mesmo intervalo, use agora o cos(x) como abscissa e o sen(x) como ordenada.
Pesquise a função sobre axes no matplotlib (ou como foi feito no exemplo 7) 
para deixar o gráfico quadrado, mesma proporção largura x altura, 
caso contrário o círculo parecerá uma elipse.
'''

import matplotlib.pyplot as plt
import numpy as np

intervalo = np.linspace(-np.pi, np.pi, 100)
cos = np.cos(intervalo)
sen = np.sin(intervalo)

plt.title('Sen(x) vs Cos(x)')
plt.xlabel('Cos(x)')
plt.ylabel('Sen(x)')
plt.plot(cos, sen)
plt.axis("scaled")  # força a mesma escala/proporção (largura x altura)
""" plt.xlim(-2, 2)
plt.ylim(-2, 2) """
plt.show()