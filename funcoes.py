# calculadora utilizando pequenas funções aritméticas!

# Definição das funções 
def soma (a,b):
    s = float
    s = a + b
    return (s)
    

def sub (a,b):
    su = float
    su = a - b
    return (su)


def mult (a,b):
    mul = float
    mul = a * b
    return (mul)


def div (a,b):
    di = float
    di = a / b
    return (di)


# programa principal
r = int(0)
sair = ('w')
while (sair != 'n') or (sair != 'N'):
    n1 = float(input('digite o 1º nº: '))
    print('=' * 30)
    op = int(input('digite a operação\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão: '))
    print('=' * 30)
    n2 = float(input('digite o 2º nº: '))
    if (op == 1):
        r = soma (n1,n2)
        print (r)
    elif (op == 2):
        r = sub (n1,n2)
        print(r)
    elif (op == 3):
        r = mult (n1,n2)
        print(r)
    elif (op == 4) and (n2 != 0):
        r = div (n1,n2)
        print (r)
    else:
        print('digite números válidos!')

    sair = input('digite (n) ou (N) P/sair: ')
    if (sair == 'n') or (sair == 'N'):
        break