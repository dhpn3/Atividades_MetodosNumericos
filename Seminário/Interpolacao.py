import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

#Codar aqui a interface de requisição de dados
def MetodoNewton():
    quant_pontos = int(input('Quantidade de pontos: ')) #Solicitando dados do usuário
    pontos, f_pontos = [],[] #Listas para armazenar os pontos e X e os valores equivalente de f(pontos) respectivamente
    tabela = [] #Lista para guardar a tabela das diferenças dividas

    #Solicitando dados do usuário
    for i in range (quant_pontos):  
        ponto = float(input('x%d= '%i))
        f_ponto = float(input('f(x%d)= '%i))

        #adicionando os valores nas respectivas listas
        pontos.append(ponto)
        f_pontos.append(f_ponto)

    tabela.append(f_pontos)
    print()
    
    #Pedindo pro usuário o ponto a ser estimado
    x = float(input('Ponto x a ser estimado: '))
    print()

    #Codar aqui a lógica de resolução do polinômio
    #Começando a calcular a tabela das diferenças divididas
    passo = 1
    for n in range (quant_pontos - 1):
        ordem = []
        for m in range (len(tabela[n])-1):
            dif_dividida = (tabela[n][m+1] - tabela[n][m]) /    (pontos[m+passo] - pontos[m])
            ordem.append(dif_dividida)
        tabela.append(ordem)
        passo += 1

    #printando a ordem
    for k in range (len(tabela)): #cada linha guarda uma ordem
        print('Ordem %d:'%k, tabela [k])
    print()

    #Calculando as aproximaçãoes usando os dados da tabela de diferença dividida
    aprox = 0
    grau = 0
    for i in range(len(tabela)):
      fator = tabela[i][0]
      for j in range (grau):
        fator *= (x-pontos[j])
      grau +=1
      aprox += fator
    print ('A aproximação encontrada para f(%f)=%f' %(x, aprox))

    # deveria ter um plot com pontos.append(x) e f_pontos.append(aprox)
    # plt.plot(x, aprox, color = 'blue', label = "Interp Linear")

    #adicionando a função teste (parábola)
    xfuncao = np.linspace(-2, 2, 50)
    yfuncao = xfuncao**2

    plt.plot(pontos, f_pontos, 'ro', label = "Medição")
    plt.plot(x, aprox, "D", color = 'gold', alpha = 1, label = "Estimativa")
    plt.plot(pontos, f_pontos, marker = '.', color = 'blue', linewidth=0.5, label = "Ligação") #aqui viria o plot da interpolação
    plt.plot(xfuncao, yfuncao, color = 'green', label = "f(x) = x²")
   
    plt.legend()
    plt.show()

MetodoNewton()