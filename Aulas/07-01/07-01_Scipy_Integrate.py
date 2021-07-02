import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def f(x):
    return x**2

areaAprox = integrate.quad(f, 0, 4)
print("Tupla recebida: ", areaAprox)
titulo = 'Area Aproximada x^2, de 0 a 4: ' + str(round(areaAprox[0], 4))
titulo += '\nErro estimado: ' + str(areaAprox[1])

x = np.linspace(0, 4, 20)
plt.plot(x, f(x))
plt.fill_between(x, f(x), color = "blue", alpha = 0.5, hatch = '|')
plt.title(titulo)
plt.show()