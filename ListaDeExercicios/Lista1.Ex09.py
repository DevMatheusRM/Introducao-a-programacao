#Exercício do Volume de uma Esfera: Escreva um programa em Python que solicite ao usuário o raio de uma esfera.
#Calcule o volume dessa esfera usando a fórmula V = (4/3) * pi * r³, onde pi é uma constante aproximada de 3.1415. Exiba
#o volume calculado na tela.
import math

pergunta = float(input('Digite o raio da esfera e calcularei o volume dessa esfera:'))
v = ((4/3)*math.pi*(pergunta**3))
print(f'O raio de esfera é de: {v:.2f}.')