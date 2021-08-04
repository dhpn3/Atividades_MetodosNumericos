import matplotlib.pyplot as plt
import csv

'''
5) Em seu programa de planilha (Excel ou Cal ou ?), crie uma planilha contendo duas colunas,
   x e f(x), e crie uma tabela para a função xˆ2 -4x + 3, com x no intervalo [0, 4] com 100 pontos.
   Salve a planilha no formato CSV.
   Verifique como importar arquivos .csv e plote o gráfico de f(x) 
   com os dados x e f(x) previamente calculadoa na planilha.
   Opções: usar módulo csv do Python (import csv -> csv.reader) ou 
   função de leitura NumPy (np.loadtxt).
'''

x = [] # criando vetores vazios
y = []

with open('Exercicio_05.csv') as csv_file:  # abrindo com a biblioteca csv
    csv_reader = csv.reader(csv_file, delimiter=';')    # lendo csv

    for linha in csv_reader:
        y.append(float(linha[0]))   # sobrepondo os valores dentro do vetor criado anteriormente
        x.append(float(linha[1]))

graf = plt.axes()   # mostra os eixos e centraliza
graf.spines.left.set_position('center') # centralizando 
graf.spines.right.set_position('center')
graf.spines.bottom.set_position('center')
graf.spines.top.set_position('center')

plt.plot(x, y, color = 'r', label='x² - 4x + 3')

plt.legend()
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title('Manipulação de arquivo CSV')
plt.ylabel('f(x)', loc='top')
plt.xlabel('x', loc='right')
plt.show()

# entrar na pasta " cd Atividades_MetodosNumericos", para executar o open()