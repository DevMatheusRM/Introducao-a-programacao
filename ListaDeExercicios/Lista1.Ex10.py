#Exercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em
#metros e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura *
#altura). Exiba o resultado do IMC na tela.

print('Dê sua altura em metros e o peso em quilogramas e lhe darei o cálculo do IMC:')
altura = float(input('Sua altura em metros é em:'))
peso = float(input('Seu peso em quilogramas é:'))
calculo = (peso/(altura*altura))
print(f'Seu IMC é: {calculo:.2f}')
