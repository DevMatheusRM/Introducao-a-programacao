# Lista de clubes populares de futebol
clubes_populares = ['Vasco', 'Flamengo', 'Palmeiras', 'Corinthians', 'Atletico-MG',
                    'Fluminense', 'Real Madrid', 'Barcelona', 'Inglaterra', 'Treze']

# Loop externo que percorre cada índice da lista de clubes populares
for indice in range(len(clubes_populares)):

    # Loop interno que percorre cada letra do clube no índice atual
    for letra in clubes_populares[indice]:
        # Imprime cada letra do clube
        print(letra)

    # Imprime o nome do clube e o tamanho do nome do clube (número de caracteres)
    print(f'{clubes_populares[indice]}, tamanho: {len(clubes_populares[indice])}')

#lista vs vetores: Geralmente não se vê.
#Porém, como volume grande de dados, o vetor separa um espaço sequencial na memoria,
#sendo mais rápido e direto. Cada microsegundo conta. SO USA "FOR"
#Já a lista existem estruturas específicas como append e etc...
