#Agora, o professor deseja sortear da lista embaralhada quem será o primeiro apresentar o trabalho.
#Faça um programa que leia o nome dos alunos, embaralhe a ordem de apresentação e sorteie
#um destes alunos para apresentar primeiro.
import random

nomes = []

while True:
    nome = input('Digite seu nome: ')
    if nome != "fim":
        nomes.append(nome)
    else:
        break

sorteados = random.sample(nomes, len(nomes))
escolhido = random.choice(sorteados)
print(f"Aluno sorteado: {escolhido}")