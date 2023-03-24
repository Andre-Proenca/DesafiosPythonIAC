# Desenvolva um método que imprima a soma dos números de 1 até 1000.

soma = 0
for contador in range(1, 1001):
    soma = soma + contador
    print(f'{soma}')
