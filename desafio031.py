#Desenvolva um método que verifique se um número informado é:
#Se é par ou ímpar
#Se é multiplo de 2
#Se é multiplo de 3
#Se é multiplo de 5

def verifica_par(numero):
    if numero % 2 == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é ímpar')

def verifica_multiplo(numero):
    if numero % 2 == 0:
        print(f"O numero {numero} é multiplo de 2")
    if numero % 3 == 0:
        print(f"O numero {numero} é multiplo de 3")
    if numero % 5 == 0:
        print(f"O numero {numero} é multiplo de 5")


numero = int(input('Digite um numero: '))
verifica_par(numero)
verifica_multiplo(numero)



