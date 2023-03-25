#  Crie uma lista com os nomes de uma turma de 10 alunos. Em seguida, desenvolva um método que solicite
#  a altura, e o código da matrícula de cada aluno, armazenando em listas paralelas.
#  Por fim, mostre a altura e o código da matrícula, do aluno mais alto, e do aluno mais baixo.

nomes = ["Andre", "Clara", "Thayssa", "Jose", "Abel"]
alturas = []
matriculas = []
maior = 0
menor = 10

for i in nomes:
    altura = float(input(f'Informe a altura do aluno(a) {i}: '))
    cod_matricula = input(f'Informe o cod da matricula do aluno(a) {i}: ')
    alturas.append(altura)
    matriculas.append(cod_matricula)
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

maiorPos = alturas.index(maior)
menorPos = alturas.index(menor)

print(f'Altura do maior aluno> Código da matricula: {matriculas.__getitem__(maiorPos)} | Altura: {alturas.__getitem__(maiorPos)}')
print(f'Altura do menor aluno> Código da matricula: {matriculas.__getitem__(menorPos)} | Altura: {alturas.__getitem__(menorPos)}')
