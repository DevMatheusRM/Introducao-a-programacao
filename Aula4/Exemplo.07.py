lista_clubes_populares = ['Vasco','Flamengo','Palmeiras','Corinthians','Atletico-MG',
                          'Fluminense','Real Madrid', 'Barcelona','Inglaterra','Treze',]

clube_coracao= input('Digite o seu clube do coração:').strip().lower().title()
presenca = False

for clube in range(len(lista_clubes_populares)):

    if clube_coracao == lista_clubes_populares[clube]:
        presenca = True

if presenca:
    print('Achei')
else:
    print('Não achei!')