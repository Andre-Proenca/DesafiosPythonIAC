# Utilizando uma lista de nomes de funcionários previamente carregada, desenvolva um método que solicite
# o salário de cada um, e armazene em uma lista paralela. Em seguida, calcule e exiba o salário
# reajustado, de acordo com a seguinte regra: Salário até R$ 300,00, reajuste de 50%;
# Salários maiores que R$ 300,00, reajuste de 30%.


def solicitar_salario():
    for i in lista_nomes:
        salario = float(input(f'Digite o salario do {i}: '))
        lista_salarios.append(salario)

    for i in range(len(lista_salarios)):
        reajustado = 0
        novo = lista_salarios[i]
        if novo <= 300:
            reajustado = novo + (novo * 0.5)
        elif novo > 300:
            reajustado = novo + (novo * 0.3)



        print(f'O novo salario do {lista_nomes[i]} sera de: {reajustado}')

lista_nomes = ['eu', 'tu', 'ele']
lista_salarios = []
solicitar_salario()
