'''
2) Considerando o array numpy abaixo (matriz 3x5):
   np.array([[5,4.5,7,5.2,6.1], [2.1,6.5,8,7,6.7], [8.6,7,9.1,8.7,9.3]])

   Elabore um programa que calcule e mostre a soma de cada linha
   armazenando o valor na respectiva posição de um vetor de 3 posições,
   ou seja, soma do valores da linha 0, na posição 0 do vetor etc.
   Calcule e mostra a média da matriz usando as somas parciais deste vetor.
'''

import matplotlib.pyplot as plt
import numpy as np

mA = np.array([[5,4.5,7,5.2,6.1], [2.1,6.5,8,7,6.7], [8.6,7,9.1,8.7,9.3]])
print(f'\n', mA, '\n')