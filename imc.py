# exercício para realizar o calculo do imc
continua = 's'
# variável continua criada com um valor qualquer

while (continua != 'n') or (continua != 'N'):
        peso = float(input('digite seu peso: '))
        alt = float(input('digite sua altura: '))
        imc =  peso / (alt ** 2)
        if (imc < 18.5):
                print('está abaixo do peso')
        elif (imc >= 18.6) and (imc <= 24.9):
                print('está com o peso normal')
        elif (imc >= 25.0) and (imc <= 29.9):
                print('peso em excesso')
        elif (imc >=30.0) and (imc <= 34.9):
                print('obesidade grau 1')
        elif (imc >= 35.0) and (imc <= 39.9):
                print('obesidade grau 2')
        elif (imc > 40):
                print('obesidade grau 3')
        continua = input('digite n ou N p/ sair:')
        # variável "continua" recebe um input do usuário, para saber se ele deseja encerrar o programa ou realizar outro.
        if (continua == 'n') or (continua == 'N'):
                break
