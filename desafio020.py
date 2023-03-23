#Desenvolva um método que solicite a entrada de uma frase, após isto troque
#todas as letras ‘A’ ou ‘a’ por &. Para tanto, pesquise como funciona o método
#String.Replace().

nome = input('Digite seu nome: ')

nova = ''

if nome.count('A') > 0 or nome.count('a') > 0:
    nova = nome.replace("A", "&")
    outra = nova.replace("a", "&")

print(f'{outra}')


