#Desenvolva um método que calcule o consumo de combustível, ou seja a
#quantidade de litros consumidos em uma viagem de veículo.

distancia = int(input('Informe a distância percorrida (Km): '))
kmLitro = float(input('Informe o consumo (Km/L): '))

def calcConsumo(distancia, kmLitro):
    res = distancia/kmLitro
    return res

consumo = calcConsumo(distancia, kmLitro)

print(f'Foram consumidos {consumo:.2f}L de combustível')
