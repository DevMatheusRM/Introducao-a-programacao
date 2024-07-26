#Classificador de Triângulos: Faça um programa que receba os comprimentos dos três lados de um triângulo e classifique-o
#como equilátero, isósceles ou escaleno.

from time import sleep
print('----Inicializando sistema----')
sleep(0)

lado1=float(input('Digite o lado 1 do triângulo:'))
lado2=float(input('Digite o lado 2 do triângulo:'))
lado3=float(input('Digite o lado 3 do triângulo:'))

if lado1 == lado2 == lado3:
    print('O seu triângulo é equilátero!')
elif lado1 != lado2 == lado3:
    print('O seu triângulo é isóceles')
elif lado1 != lado2 != lado3:
    print('O seu ângulo é escaleno')

print('----Finalizando Sistema----')