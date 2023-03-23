# o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.
import random

nomes = []

while True:
    nome = input('Digite o nome dos alunos: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break

sorteados = random.sample(nomes, len(nomes))

for valor in sorteados:
    print(f"Aluno sorteado: {valor}")
