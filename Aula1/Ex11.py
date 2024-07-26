#Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando R
#$1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
#ficará por R $1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
#compra.

quantidade_macas = int(input('Digite quantas maças deseja comprar:'))

if quantidade_macas <= 5:
    print(f'Valor total R$ {quantidade_macas * 1.37}.')
else:
    print(f'10% de desconto aplicado!'
          f' Valor total R$ {quantidade_macas * 1.24:.2f}')
