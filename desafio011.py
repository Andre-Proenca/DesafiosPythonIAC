#um professor quer armazenas o nome dos seus alunos para realizar algumas
#tarefas. Faça um programa que ajude ele, lendo o nome deles e escrevendo todos os nomes armazenados.

nomes = []

while True:
    nome = input('Digite seu nome: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break

for valor in nomes:
    print(f'Aluno: {valor}')