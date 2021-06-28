'''
- Lista de Exercícios I - 

Usando MatPlotLib e NumPy implemente os seguintes exercícios para exploração 
e fixação de comandos e métodos destes módulos.

1) Utilizando sen, cos e linspace do NumPy mais matplotlib, calcule e apresente o gráfico
   de sen(x) e de cos(x) no intervalo [-PI, +PI] no mesmo plot (pegando PI do NumPy). 
   Use plot e show de forma básica.

2) Utilizando o mesmo intervalo, use agora o cos(x) como abscissa e o sen(x) como ordenada.
   Pesquise a função sobre axes no matplotlib (ou como foi feito no exemplo 7) 
   para deixar o gráfico quadrado, mesma proporção largura x altura, 
   caso contrário o círculo parecerá uma elipse.

3) Empregando sen(x) no mesmo intervalo, mas agora usando np.arange (com passo 0.2), 
   plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plor de 0.2,
   ou sejam sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
   Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)

4) Plote a curva dada por:
   x = sen t
   y = 2 sen 4t
   Com t no intervalo [0, 2PI] com 100 pontos.

5) Plote o polinômio:
   f(x) = 4xˆ5 -12xˆ3 -6x^2 -x -2
   Com x no intervalo [-2, 2] com 200 pontos. 
   Coloque o f(x) em uma função: 
   def f(x): 
      # retorno da equação
   Antes de plt.show(), chame plt.grid().
'''
