'''
3) Empregando sen(x) no mesmo intervalo, mas agora usando np.arange (com passo 0.2), 
plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plot de 0.2,
ou sejam sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)
'''

import matplotlib.pyplot as plt
import numpy as np

phi = 0.2

x = np.arange(-np.pi, np.pi, phi)
sen1 = np.sin(x) #sen(x)
sen2 = np.sin(x-phi) #sen(x-0.2)
sen3 = np.sin(x-2*phi) #sen(x-0.4)
sen4 = np.sin(x-3*phi) #sen(x-0.6)
sen5 = np.sin(x-4*phi) #sen(x-0.8)
sen6 = np.sin(x-5*phi) #sen(x-1)

plt.title('Sen(x-n), 0 ≤ n ≤ 1')
plt.plot(x, sen1, ls = '-', color = 'red') #default sen(x)
plt.plot(x, sen2, ls = '--', color = 'yellow')
plt.plot(x, sen3, ls = ':', color = 'green')
plt.plot(x, sen4, ls = '-.', color = 'blue')
plt.plot(x, sen5, marker = '.', color = 'hotpink') # ora usar '.' e 'o' só como marker, linestyle n permite.
plt.plot(x, sen6, marker = 'o', color = 'grey')
plt.show()