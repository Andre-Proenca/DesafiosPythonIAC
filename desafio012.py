#o mesmo professor quer agora, além de exibir, ordenar a lista. Faça um
#programa que ajude ele, lendo o nome deles e escrevendo todos os nomes armazenados, de forma ordenada.

nomes = []

while True:
    nome = input('Digite seu nome: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break
nomes.sort()

for valor in nomes:
    print(f'Aluno: {valor}')