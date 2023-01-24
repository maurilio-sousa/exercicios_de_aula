# criando uma tabuada utilizando o laço de repetição for

num = int(input('digite um nº para ver sua tabuada: '))
for i in range (1, 11):
    print('{} x {} = {}'. format(i,num, num*i))
