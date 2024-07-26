#Comparador de Números: Crie um programa que receba dois números do usuário e determine qual deles é o maior ou se
#são iguais

from time import sleep
print('----Inicializando sistema----')
sleep(2)

valor1=float(input('Digite um número:'))
valor2=float(input('Digite um número:'))

if valor1>valor2:
    print(f'O número {valor1} é maior que {valor2}.')
elif valor1<valor2:
    print(f'O número {valor2} é maior que {valor1}')
else:
    print(f'Os número {valor1} e {valor2} são iguais.')

print('----Finalizando Sistema----')