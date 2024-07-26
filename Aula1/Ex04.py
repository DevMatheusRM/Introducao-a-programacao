#Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o percentual de
#desconto. Calcule o valor do desconto e exiba o valor final após o desconto.
valorproduto=float(input('Digite aqui o valor do produto:'))
valordesconto=float(input('Digite aqui o valor do desconto:'))
calculo1=((valorproduto*valordesconto)/100)
calculo2=(valorproduto-calculo1)
print(f'O valor final com desconto aplicado é de: {calculo2}')