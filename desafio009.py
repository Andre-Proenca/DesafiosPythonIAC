# escreva um programa que converta uma temperatura digitada em graus
#celsius para fahrenheit

celsius = float(input('Por favor digite a temperatura em celsius: '))
far = ((celsius * 9)/5) + 32
print(f'O grau em fahrenhet é : {far:.2f}ºF')
