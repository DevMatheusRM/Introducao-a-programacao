#Exercício da Média: Escreva um programa em Python que solicite ao usuário duas notas e calcule a média entre elas.
#Em seguida, exiba o resultado na tela.
valor1=int(input('Digite o valor da nota 1:'))
valor2=int(input('Digite o valor da nota 2:'))
resultado=((valor1 + valor2)/2)
print(f'A sua média é: {resultado:.1f}')