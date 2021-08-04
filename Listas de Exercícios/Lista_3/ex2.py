import numpy as np
import matplotlib.pyplot as plt

passos = float(input('Insira os passos (1, .5, .25, .125, .1, .0625, .05, .04, .03125, .025, .0125):\t'))
x = np.arange(0, 24.5, passos)
y, riemann = [], []

for i in x:

    if 0 <= i <= 3:
        funcao = 3 * i
        y.append(funcao)
        riemann.append(funcao * passos)
    if 3 < i <= 6 or 18 < i <= 21:
        funcao = 10
        y.append(funcao)
        riemann.append(funcao * passos)
    if 6 < i <= 18:
        funcao = (i/2 - 6)**2
        y.append(funcao)
        riemann.append(funcao * passos)
    if 21 < i <= 25:
        funcao = 73 - 3*i
        y.append(funcao)
        riemann.append(funcao * passos)

riemann = sum(riemann)

plt.plot(x, y, color = 'black')
plt.fill_between(x, y, alpha=0.2, color = 'green', hatch='|')
plt.title(riemann)

plt.show()