import matplotlib.pyplot as plt
import numpy as np

'''
def f(x):
    return x

def g(x):
    return x**2

x = np.linspace(0, 1, 50)
plt.plot(x, f(x))
plt.plot(x, g(x))

# plt.fill_between(x, f(x), color = "grey", alpha = 0.5, hatch = '|') # interpreta a área ENTRE 2 gráficos 
# plt.fill_between(x, g(x), color = "yellow", alpha = 0.2, hatch = 'O') # interpreta a área ENTRE 2 gráficos 

plt.fill_between(x, f(x), g(x), color = "lightpink", alpha = 0.4, hatch = '-')
plt.show()
'''

def f(x):
    return -x**2 + 12

def g(x):
    return x**2 -6

x = np.linspace(-4, 4, 50)
plt.plot(x, f(x))
plt.plot(x, g(x))
# plt.fill_between(x, f(x), g(x))

fill = np.linspace(-3, 3, 50)

plt.fill_between(fill, f(fill), g(fill), color = "grey", alpha = 0.3, hatch = '|')
plt.show()