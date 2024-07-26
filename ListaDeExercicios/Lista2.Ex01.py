#Verificador de Número Par ou Ímpar: Crie um programa que verifique se um número (informado pelo usuário) é par ou
#ímpar.

from time import sleep
print('----Inicializando sistema----')
sleep(2)

valor=float(input('Digite um número'))
if valor % 2 == 0:
    print('O seu valor é par')
else:
    print('O seu valor é impar!')

print('----Finalizando Sistema----')