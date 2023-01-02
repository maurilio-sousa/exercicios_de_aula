# execício proposto pelo professor.
# usarmos a equação de bhaskara para calcularmos ás raízes dde uma parábola.

#importando biblioteca para usarmos a fórmula do delta
import math
a = float(input('digite o valor de A: '))
b = float(input('digite o valor de B: '))
c = float(input('digite o valor de C: '))
delta = b**2 - 4 * a * c
if (delta < 0) :
    print('Não tem raízes reais')
elif (delta == 0):
    x = -b / (2 * a)
    print('Temos como solução duas raízes iguais para o valor de X: {}'. format(x))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('Temos como solução duas raízes reais e diferentes')
    print('x1 = {:.2f}'. format(x1))
    print('x2 = {:.2f}'. format(x2))

