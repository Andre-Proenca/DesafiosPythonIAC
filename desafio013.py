#O mesmo professor quer sortear um dos seus alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

nomes = []

while True:
    nome = input('Digite seu nome: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break
nomes.sort()
aluno = random.choice(nomes)

for valor in nomes:
    print(f'Aluno selecionado: {aluno}')
