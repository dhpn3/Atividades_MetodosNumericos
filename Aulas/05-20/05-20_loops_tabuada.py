# treinando loops

# tabulada do número N

# loop usando while
'''
n = int(input("Digite o numero para ver sua tabuada: "))
i = 1

while i <= 10:
    print(f'{i} x {n} = {i*n}')
    i = i + 1
'''


#loop usando for
'''
n = int(input("Digite o numero para ver sua tabuada: "))
#for i in [1,2,3,4,5,6,7,8,9,10]:

i = 1
for i in range(1, 11, 1):   #usando função range()
    print(f'{i} x {n} = {i*n}')
'''

#exercicio 10 tabuadas
for n in range(1,11,1):
    print(f"\n--- Tabuada do {n} ---\n")
    for i in range(1, 11, 1):
        print(f'{i} x {n} = {i*n}') # vai ser executada 10 vezes pra cada N, ou seja, 100 vezes