#Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL) e
#faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL. Exiba o
#valor convertido na tela

pergunta = float(input('Conversor de moeda! Escreva seu valor em R$ e passarei para U$ (Dólar):'))
calculo = (pergunta/5)
print(f'O seu montante em dólares é de U$ {calculo} dólares americanos.')