#Desenvolva um método que identifique o maior e o menor número dentre 5
#números fornecidos pelo usuário.

numeros = []
i=0

while i<5:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    i = i + 1

print(numeros)

print(f'\nO maior número é {max(numeros)} e o menor número é {min(numeros)}')
