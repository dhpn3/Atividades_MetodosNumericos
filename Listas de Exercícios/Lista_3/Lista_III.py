'''
- Lista de Exercícios III - 

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


2) Desenvolva o mesmo algoritmo, agora usando um conjunto de funções 
   livremente escolhidas que graficamente simulem um pista de skate, 
                __ __
   algo como:  /  U  \

   Identifique as funções, algo como 4 segmentos de reta e uma parábola, 
   calcule a área usando a soma de Riemman, permitindo a escolha da 
   base do retângulo (o passo). 
   Escolha apenas uma aproximação para altura (esquerda, central ou direita),
   como melhor achar conveniente.
   Plote o gráfico apenas com fill-beetween (não precisa representar as barras).
   Idealmente, apresente no gráfico a legenda de cada função utilizada,
   a área aproximada calculada e se calculada analiticamente, a área exata
   resultante da integração.

'''