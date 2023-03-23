#Desenvolva um método que permita a entrada do nome do usuário e exiba:
#Imprima a frase “Olá meu nome é: {nome recebido}”.
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

qtdLetras = nome.replace(" ", "").count()

qtdePrimeiroNome = len(nome.split()[0])

print(f'Olá seu nome é: {nome}\n'
      f'Nome em maiúsculas: {nome.upper()}\n'
      f'Nome em minúsculas: {nome.lower()}\n'
      f'Seu nome tem {qtdLetras} letras\n'
      f'O primeiro nome tem {qtdePrimeiroNome} letras')
