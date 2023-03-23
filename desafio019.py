#Desenvolva um método que solicite a entrada da idade de um determinado
#usuário, se for menor que 18 anos exiba na cor vermelha “Sem permissão”, caso seja maior
#ou igual a 18 anos exiba na cor verde “Permissão concedida”. Para tanto, pesquise como
#funciona o uso de cores no Python.

def verificaIdade():
    RED = "\033[1;31m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    idade = int(input('Digite sua idade'))
    if idade < 18:
        print(f'{RED} sem permissao {RESET} ')
    else:
        print(f'{GREEN} com permissao {RESET} ')

verificaIdade()
