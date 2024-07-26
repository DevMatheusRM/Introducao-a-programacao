#Imagine que você está desenvolvendo um sistema para um programa de rádio esportivo.
# Os ouvintes podem ligar e tentar adivinhar se o nome do seu clube do coração está na lista dos 10 clubes mais
#populares da cidade.
#Crie um algoritmo que:
#Peça para o usuário digitar os nomes de 10 clubes de futebol e armazene-os em uma lista.
#Solicite ao usuário que digite o nome de um clube qualquer.
#Verifique se o nome do clube está na lista dos 10 clubes mais populares.
#Imprima "ACHEI!" se o clube estiver na lista,
#ou "NÃO ACHEI!" caso contrário, para que o apresentador do programa possa informar o ouvinte ao vivo.

lista_clubes_populares = ['Vasco','Flamengo','Palmeiras','Corinthians','Atletico-MG',
                          'Fluminense','Real Madrid', 'Barcelona','Inglaterra','Treze',
                          'Ibis']

clube_coracao= input('Digite o seu clube do coração:').strip().lower().title()

for clube in range (1,11):
    if clube == clube_coracao:
        print(f'Achei o {clube}!')
    else:
        print(f'Não achei o {clube}!')


lista_ouvinte = []
print(lista_ouvinte)

