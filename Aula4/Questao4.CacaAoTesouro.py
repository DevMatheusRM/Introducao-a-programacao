#Imagine um mapa do tesouro dividido em 25 quadrados (5 linhas e 5 colunas).
#Cada quadrado esconde um número, representando a quantidade de moedas de ouro enterradas ali.
#Sua missão é encontrar o quadrado com o maior tesouro!

#Crie um algoritmo que: Leia os números que representam a quantidade de moedas em cada quadrado do mapa (matriz 5 x 5).
#Vasculhe o mapa em busca do quadrado com o maior número de moedas.
#Indique a posição exata desse quadrado (linha e coluna), marcando o local onde o maior tesouro está escondido.

from random import randint

# Inicializa a lista que representará o mapa do tesouro
mapa_do_tesouro = []

# Cria o mapa do tesouro, que é uma matriz 5x5
for i in range(5):  # Loop para cada linha do mapa
    lista_temporaria = []  # Cria uma lista temporária para armazenar os valores de uma linha

    for j in range(5):  # Loop para cada coluna da linha
        # Adiciona um número aleatório entre 1 e 200 à lista temporária
        lista_temporaria.append(randint(1, 200))

    # Adiciona a lista temporária (linha) ao mapa do tesouro
    mapa_do_tesouro.append(lista_temporaria)

# Resolução do problema: encontrar o quadrado com o maior tesouro

bau_tesouro = 0  # Inicializa o valor do maior tesouro encontrado
posicao = []  # Inicializa a posição do maior tesouro encontrado

for linha in range(len(mapa_do_tesouro)):  # Loop por cada linha do mapa
    for coluna in range(len(mapa_do_tesouro[linha])):  # Loop por cada coluna da linha
        # Verifica se o valor atual é maior que o maior tesouro encontrado
        if mapa_do_tesouro[linha][coluna] > bau_tesouro:
            bau_tesouro = mapa_do_tesouro[linha][coluna]  # Atualiza o valor do maior tesouro
            posicao = [linha + 1, coluna + 1]  # Atualiza a posição do maior tesouro

# Imprime o maior valor encontrado no mapa
print(f'O maior valor do mapa é: {bau_tesouro}')
# Imprime a posição do maior valor no mapa (linha e coluna)
print(f'A posição no mapa é: {posicao}')
# Imprime a matriz completa do mapa do tesouro
print(mapa_do_tesouro)
