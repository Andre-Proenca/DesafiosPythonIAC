#Faça um programa que leia um número inteiro e mostre na sua tela a sua tabuada.

cont = [1,2,3,4,5,6,7,8,9,10]
valor = int(input("Digite um número para imprimir sua tabuada: "))
print(f'A tabuada do número {valor} é:')

for i in cont:

    print(f'{valor} x {i} =  {valor * i}')
