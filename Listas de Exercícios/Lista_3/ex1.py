"""

1) Calculando área aproximada

   Empregando a função f(x) = 2x, integrada no intervalo [1, 4],
   tem-se como solução analítica 15.

   Elabore um programa que aplique a Soma de Riemann para estimar a área
   solicitando ao usuário o tamanho do passo (base do retângulo), apresente
   o valor estimado da área e o erro relativo.

   Os passos devem ser frações exatas de 1, como por exemplo:
   1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125 etc
   para não extrapolarem o intervalo.

   Erro relativo = | analitico - aproximado | / | analítico |

   Plote o gráfico apresentando os retângulos, o valor aproximado e o erro
   relativo.
   Dica para plotar os retângulos: simplesmente usar plt.bar (deixando as cores sem interferir)
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

   Para comparar o resultados, crie 3 gráficos (sub plots) na mesma plotagem
   e contabilize os três valores da área calculada:
   - pegando altura pela esquerda (antes do passo)
   - pegando altura no meio (métade do passo)
   - pegando altura pela direita (depois do passo)

"""

import matplotlib.pyplot as plt
import numpy as np

area_01 = float
area_02 = float
area_03 = float


def areas_aprox():
    global area_01
    global area_02
    global area_03

    area_01 = sum(x * 2) * passos
    area_02 = sum(x * 2 + passos) * passos
    area_03 = sum(x * 2 + 2 * passos) * passos

    print('Este é a área aproximada do gráfico 01:\t', area_01)
    print('Este é a área aproximada do gráfico 02:\t', area_02)
    print('Este é a área aproximada do gráfico 03:\t', area_03)


def grafico_01():
    sub_graf.add_subplot(1, 3, 1)
    plt.bar(x, funcao, color=cores, align='edge', width=passos)
    plt.plot(x, funcao, marker='o', color='black')
    plt.xticks([1, 2, 3, 4])
    plt.xlim(0, 5, 1)
    plt.title(f'Área Aproximada: {area_01}\n'
              f'Área Calculada: {15}\n'
              f'(Erro: {(abs(float(area_01) - 15) / 15) * 100}%)')


def grafico_02():
    sub_graf.add_subplot(1, 3, 2)  # Adiciona o subplot o gráfico seguinte (.,., posic)
    plt.bar(x, funcao + passos, color=cores, align='edge', width=passos)  # width=1.3
    plt.plot(x + passos / 2, funcao + passos, marker='o', color='black')
    plt.xticks([1, 2, 3, 4])
    plt.xlim(0, 5, 1)
    plt.title(f'Área Aproximada: {area_02}\n'
              f'Área Calculada: {15}\n'
              f'(Erro: {(abs(float(area_02) - 15) / 15) * 100}%)')


def grafico_03():
    sub_graf.add_subplot(1, 3, 3)  # Adiciona o subplot o gráfico seguinte (.,., posic)
    plt.bar(x, funcao + 2 * passos, color=cores, align='edge', width=passos)  # width=1.3
    plt.plot(x + passos, funcao + 2 * passos, marker='o', color='black')
    plt.xticks([1, 2, 3, 4])
    plt.xlim(0, 5, 1)
    plt.title(f'Área Aproximada: {area_03}\n'
              f'Área Calculada: {15}\n'
              f'(Erro: {(abs(float(area_03) - 15) / 15) * 100}%)')


print('Dentre estes valores: 1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125\n')
passos = float(input('Insira o número de passos:\t'))

x = np.arange(1, 4, passos)
funcao = 2 * x
areas_aprox()

cores = ['blue', 'red', 'black', 'orange']
sub_graf = plt.figure()

grafico_01()
grafico_02()
grafico_03()

plt.show()