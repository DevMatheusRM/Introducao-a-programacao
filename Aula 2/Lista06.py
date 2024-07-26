#Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando R
#$1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
#ficará por R $1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
#compra.

quantidade_macas=int(input('Olá! Quantas maçãs você deseja?!'))

if quantidade_macas == 1:
    print(f'O custo desta maça é de R$ 1,24!')
elif 1 < quantidade_macas < 12:
    print(f'O custo destas maças foi de R$ {quantidade_macas * 1.24}!')
elif quantidade_macas >= 12:
    calculo_de_desconto=((quantidade_macas*10)/100)
    print(f'A partir de 12 maçãs você pagará 10% de desconto, ficando o valor abatido de '
          f'R$ {calculo_de_desconto + quantidade_macas}! ')
else:
    print('Valor inválido!')