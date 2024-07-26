#Exercício do Cálculo de Área: Escreva um programa em Python que solicite ao usuário a largura e a altura de um
#retângulo. Calcule a área desse retângulo e exiba o resultado.

largura = float(input('Descreva a largura de um retângulo:'))
altura = float(input('Descreva a altura de um retângulo:'))
calculo = (largura*altura)
print(f'O resultado da área do retângulo é de: {calculo:.2f} cm.')