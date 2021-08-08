import numpy as np
import matplotlib.pyplot as plt

passos = float(input('Insira os passos (1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125):\t'))
intervalo = np.arange(0, 24.5, passos)
fx, soma_riemann = [], [] # dois vetores vazios

for i in intervalo:     # de 0 a 24.5, com passo igual a 'passos'

    if 0 <= i <= 3:     # primeira reta crescente de x=0 até x=3 (3 pontos)
        funcao = 3 * i
        fx.append(funcao)
        soma_riemann.append(funcao * passos)

    if 3 < i <= 6 or 18 < i <= 21:      #reta constante de 3 até 6, e depois da parábola, de 18 até 21
        funcao = 10
        fx.append(funcao)
        soma_riemann.append(funcao * passos)    #acrescenta o valor da área no vetor 'soma_riemann'
        
    if 6 < i <= 18:     # parábola (x/2 - 6)²
        funcao = (i/2 - 6)**2
        fx.append(funcao)
        soma_riemann.append(funcao * passos)    #acrescenta o valor da área no vetor 'soma_riemann', através da conta 'função*passos', ou seja, (x/2 - 6)² * passos (base vs altura) 

    if 21 < i <= 25:        # reta decrescente de x = 21 até x = 25 (3 pontos)
        funcao = 73 - 3*i
        fx.append(funcao)
        soma_riemann.append(funcao * passos)

soma_riemann = sum(soma_riemann)    # soma todas as áreas do vetor 'soma_riemann', ou seja 'soma_riemann = soma_riemann de todas as funções

plt.plot(intervalo, fx, color = 'black')    # plota f(x) vs x, com a cor preta
plt.fill_between(intervalo, fx, alpha=0.2, color = 'green', hatch='|')  # fill.between preenche a área abaixo da curva com cor e símbolo diferente
plt.title(f'Área pela Soma de Riemann: {round(soma_riemann, 3)}')   # título = área total de todas as funções, com aproximação de 3 decimais
plt.show()