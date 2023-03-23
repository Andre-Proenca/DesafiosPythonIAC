#Desenvolva um método que calcule o volume de um Cilindro qualquer. Para
#tanto, pesquise como calcular o volume de um cilindro.

raio = float(input('Informe o raio: '))
altura = float(input('Informe a altura: '))

volume: 3.14159 * raio **2 * altura

print(f'O volume é: {volume:.4f} m³')