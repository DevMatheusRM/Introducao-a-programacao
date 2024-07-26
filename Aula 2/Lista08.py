#Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para realizar
#esta tarefa. Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X, e também a
#quantidade real existente no estoque. Por fim, o programa deve responder se é necessário adquirir mais produtos,
#comparando o estoque real com a média entre valor máximo e mínimo.
#a. se o estoque real estiver abaixo da média, informar a necessidade de compra;
#b. se estiver acima da média informar que não precisa adquirir novos produtos;
#c. se estiver na média, informa que em breve será necessária nova aquisição de produtos;

produto = str(input('Digite o nome do produto:'))
qtd_min = int(input(f'Digite a quantidade mínima de {produto}:'))
qtd_max = int(input(f'Digite a quantidade máxima de {produto}:'))
qtd_real = int(input("Informe a quantidade real do estoque: "))

# Função para calcular a média entre máximo e mínimo
def calcular_media(maximo, minimo):
    return (maximo + minimo) / 2

# Função para verificar a necessidade de compra
def verificar_estoque(maximo, minimo, real):
    media = calcular_media(maximo, minimo)

    if real < media:
        return "É necessário adquirir mais produtos."
    elif real > media:
        return "Não precisa adquirir novos produtos."
    else:
        return "Em breve será necessária nova aquisição de produtos."


# Verificação do estoque
resultado = verificar_estoque(qtd_max, qtd_min, qtd_real)
print(resultado)
