import matplotlib.pyplot as plt # plt como apelido pro pyplot da biblioteca de plotagem de gráfico matplotlib
# www. matplotlib.org
import numpy as np


'''
plt.plot([1, 2, 3, 4], [3, 4, 7, 10]) #cria o gráfico com eixo X e eixo Y definidos
plt.show() # mostra o gráfico na tela
'''

'''
x = [-2, -1, 0, 1, 2]
y = [4, 1, 0, 1, 4]
plt.plot(x,y)
plt.show()
'''

'''
x = -10

while x <= 10:
    y = x ** 2 # x²  = parábola
    plt.plot(x, y, marker ='+', color = 'red') #montagem do gráfico e com marcação em cada ponto discreto
    x += 0.2 #passo de 0.2 em 0.2

plt.title('f(x) = x^2')
plt.xlabel('eixo x')
plt.ylabel('f(x)')
plt.show()
'''

eixoX = np.linspace(-10, 10, 200) # esse cara ja é um vetor com 200 pontos, n preciso colocar o passo pq importei o linspace do numpy
eixoY = eixoX  ** 2 # n precisei fazer o loop pra fazer os passos ou pontos até 200
#print(eixoX)
#print(eixoY)
plt.plot(eixoX,eixoY)
plt.show()