#ler um número inteiro e dizer se ele é ou não um nº primo
#se é divísivel por 2 números apenas, ele é um nº primo
num = int(input('digite um º inteiro: '))
total = 0  
for c in range (1, num+1):
    if (num % c == 0):
        print('\033[33m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'. format(c), end = ' ')
print('\no nº {} foi divisível {} vezes'. format(num, total))
if (total == 2):
    print('ele é um número primo')
else:
    print('por isso ele não é primo')

    

    
