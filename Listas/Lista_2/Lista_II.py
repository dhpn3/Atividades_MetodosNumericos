'''
- Lista de Exercícios II - 

Usando MatPlotLib e NumPy implemente os seguintes exercícios para exploração 
e fixação de comandos e métodos destes módulos.

1) Plote os dois polinômios f(x) e g(x):
   f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18
   g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24
   Com x no intervalo [-4.5, 4.5] com 300 pontos. Antes de plt.show(), chame plt.grid(). 
   Implemente as funções em código Pytho:
   def f(x): 
      # retorno da função f
   def g(x): 
      # retorno da função g     
   Coloque as equações dos polinômios como rótulos (ver exemplo 7).

2) Considerando o array numpy abaixo (matriz 3x5):
   np.array([[5,4.5,7,5.2,6.1], [2.1,6.5,8,7,6.7], [8.6,7,9.1,8.7,9.3]])
   Elabore um programa que calcule e mostre a soma de cada linha
   armazenando o valor na respectiva posição de um vetor de 3 posições,
   ou seja, soma do valores da linha 0, na posição 0 do vetor etc.
   Calcule e mostra a média da matriz usando as somas parciais deste vetor.

3) Usando NumPy, crie uma matriz mA 5x5 com numeros aleatórios no intervalo [1, 9].
   (use np.random.randint ou crie gerador com np.random.default_rng() e use o método integers,
   ver ambas opções na documentação).
   Inicialize uma matriz identidade mId 5x5 e teste a função de multiplicação de matrizes (@ ou dot)
   entre mA e MI. Faça também a transposta (transpose ou T) de mA e a inversa (I) de mA.
   Pesquise como calcular o determinante de mA (módulo linalg do numpy), mostrando o valor do determinante.

4) Crie uma função python que retorna o maior de dois números enviado por parâmetro.
   Ela irá funcionar de maneira regular, ou seja, operando sobre 2 escalares.
   Verifique o funcionamento da função NumPy vectorize, e crie então a função
   que opera sobre vetores.
   Teste sua função com dois arrays numpy de 10 posições sorteadas de números inteiros
   no intervalo [10, 100) (usando funções NumPy).
   Mostre os 3 vetores.

5) Em seu programa de planilha (Excel ou Cal ou ?), crie uma planilha contendo duas colunas,
   x e f(x), e crie uma tabela para a função xˆ2 -4x + 3, com x no intervalo [0, 4] com 100 pontos.
   Salve a planilha no formato CSV.
   Verifique como importar arquivos .csv e plote o gráfico de f(x) 
   com os dados x e f(x) previamente calculadoa na planilha.
   Opções: usar módulo csv do Python (import csv -> csv.reader) ou 
   função de leitura NumPy (np.loadtxt).
'''