#Desenvolva um método que calcule o volume de uma caixa d'água retangular.
#Para tanto, pesquise como calcular o volume de um retângulo.

alt = float(input("Informe a altura da caixa: "))
larg = float(input("Informe a largura da caixa: "))
compr = float(input("Informe o comprimento da caixa: "))

caixa = alt * larg * compr
print(f"O volume da sua caixa d'agua é: {caixa:.2f} cm³")
