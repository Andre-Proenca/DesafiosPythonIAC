#Escreva um programa que pergunte a quantidade de km percorridos por
#um carro alugado, e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
#pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Digite a qtde de km: '))
dias = int(input('Digite a qtde de dias alugados: '))
precoKm = km * 0.15
precoDias = dias * 60
preco = precoKm + precoDias
print(f'O valor do aluguel foi: R${preco:.2f}')
