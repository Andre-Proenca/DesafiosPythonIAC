#Crie uma lista com os nomes de uma turma de 20 alunos. Em seguida, elabore um método que solicite
# a idade de cada um, e armazene em uma lista paralela. Por fim, calcule a idade média da turma.

nomes = ["Andre", "Clara", "Thayssa", "Jose", "Abel"]
idades = []

def solicitar_idade():
    for i in nomes:
        idade = int(input(f'Por favor digite a idade do aluno {i}: '))
        idades.append(idade)

    media = sum(idades) / len(idades)
    print(f'A idade média da turma é: {media:.2f}')

solicitar_idade()



