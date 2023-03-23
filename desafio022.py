#Desenvolva um método que calcule o IMC de uma determinada pessoa. Para
#tanto, pesquise como funciona o cálculo do IMC.

peso = float(input('Informe o peso da pessoa em kg: '))
altura = float(input('Informe a altura da pessoa em metros: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso.')
elif (imc > 18.5) and (imc < 25.0):
    print('Peso ideal.')
elif (imc > 25.5) and (imc < 30.0):
    print('Sobrepeso.')
elif (imc > 30.0) and (imc < 40.0):
    print('Obesidade.')
elif imc > 40.0:
    print('Obesidade mórbida.')