# o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.

nomes = []

while True:
    nome = input('Digite o nome dos alunos: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break
