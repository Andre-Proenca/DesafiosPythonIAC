#Desenvolva um método que calcule o reajuste salarial. Se o salário for abaixo
#de 1.700 o ajuste é de R$300.00, se maior o reajuste é de R$ 200.00. Para finalizar, exiba o
#novo salário na tela.

def calc_reajuste(salario):
    reajuste = 0
    if salario < 1700:
        reajuste = 300
    else:
        reajuste = 200

    print(f'Seu novo salario sera de R${salario + reajuste:.2f}')

salario = float(input('Parabens voce ira receber um aumento!\n'
                      'Mas antes me diga qual seu salario atual: '))
calc_reajuste(salario)
