#Desenvolva uma calculadora, onde será necessário entrar com a operação,
#primeiro e segundo valor, exiba o resultado na tela

num1 = int(input('Digite o primeiro numero: '))
op = input('Digite a operacao: ')
num2 = int(input('Digite o segundo numero: '))

if op == '+':
    print(f'{num1} + {num2} = {num1 + num2}')

elif op == '-':
    print(f'{num1} - {num2} = {num1 - num2}')

elif op == '*':
    print(f'{num1} * {num2} = {num1 * num2}')

elif op == '/':
    print(f'{num1} / {num2} = {num1 / num2}')

