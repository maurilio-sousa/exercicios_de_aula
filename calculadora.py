# foi feita uma calculadora na ordem de uma calculadora de mão
n1 = float(input('digite o 1º número: '))
op = (input('digite a operação desejada\n+:soma\n-:subtração\n*:multiplicação\n/:divisão : '))
n2 = float(input('digite o 2º número: '))
resultado = 0
if (op == '+'):
    resultado = n1 + n2
elif (op == '-'):
    resultado =  n1 - n2
elif (op == '*'):
   resultado = n1 * n2
elif (op == '/') and (n2 != 0): 
    resultado = n1 / n2
else:
    print('não é válido divisões por 0 no dividendo') 
print('resultado: {:.1f}'.format(resultado))
