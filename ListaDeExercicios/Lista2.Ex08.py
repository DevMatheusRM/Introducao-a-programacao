#Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para realizar
#esta tarefa. Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X, e também a
#quantidade real existente no estoque. Por fim, o programa deve responder se é necessário adquirir mais produtos,
#comparando o estoque real com a média entre valor máximo e mínimo.
#a. se o estoque real estiver abaixo da média, informar a necessidade de compra;
#b. se estiver acima da média informar que não precisa adquirir novos produtos;
#c. se estiver na média, informa que em breve será necessária nova aquisição de produtos;


from time import sleep
print('----Iniciando sistema----')
sleep(1)
while True:
    try:
        produto_desejado = int(input('Consultor de estoque! Irei verificar para você: \n'
                                     ' - Escolha o produto abaixo (digite o número correspondente): \n'
                                     ' [1] CAMISETAS \n [2] CALÇAS \n [3] MEIAS \n Produto desejado: '))

        if produto_desejado not in [1, 2, 3]:
            print("Opção inválida! Por favor, escolha uma das opções listadas.")
        else:
            break  # sai do loop se a entrada for válida

    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

quantidade_real_produto=int(input('Agora descreva a quantidade real do produto:'))

print('----Carregando banco de dados----')
sleep(1)

if produto_desejado == 1:
    print(f'ESTOQUE DE CAMISETAS: \n - Quantidade máxima: 250 \n - Quantidade mínima: 1 \n --- \n '
          f'- Quantidade real: {quantidade_real_produto} \n --- \n')
elif quantidade_real_produto >= 250:
    print('Não é necessária a aquisição de novas unidades.')
elif quantidade_real_produto <= 250:
    print(f'Será necessária a aquisição de {250 - quantidade_real_produto:.0f} unidades')

if produto_desejado == 2:
    print(f'ESTOQUE DE CALÇAS: \n - Quantidade máxima: 250 \n - Quantidade mínima: 1 \n --- \n '
          f'- Quantidade real: {quantidade_real_produto} \n --- \n')
elif quantidade_real_produto >= 250:
    print('Não é necessária a aquisição de novas unidades.')
elif quantidade_real_produto <= 250:
    print(f'Será necessária a aquisição de {250 - quantidade_real_produto:.0f} unidades')

if produto_desejado == 3:
    print(f'ESTOQUE DE MEIAS: \n - Quantidade máxima: 250 \n - Quantidade mínima: 1 \n --- \n '
          f'- Quantidade real: {quantidade_real_produto} \n --- \n')
elif quantidade_real_produto >= 250:
    print('Não é necessária a aquisição de novas unidades.')
elif quantidade_real_produto <= 250:
    print(f'Será necessária a aquisição de {250 - quantidade_real_produto:.0f} unidades')

#Como fazer para que o código recuse qualquer valor de entrada no primeiro input que não seja os descritos no próprio input?