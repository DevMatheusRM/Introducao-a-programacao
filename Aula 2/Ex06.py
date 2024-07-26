
from time import sleep

print("----Iniciando o programa----")
sleep(2)

ano_nascimento = int(input('Digite o ano de seu nascimento:'))
ANO_ATUAL = 2024 #Quando boto em letras maiúsculas eu deixo a variável imutável.

idade = ANO_ATUAL - ano_nascimento

if idade >= 16:
    print('Você pode votar!')
    if idade>= 18:
        print('Você pode dirigir!')

print('----Fim do programa----')
