i = True
a = 0

while i:
    print(f'Tentativa de acesso ao Banco de Dados n: {a}')

    if (a ** 2) > 100000:
        i = False
        print('Tentativa de acesso ao BD com sucesso!')

    a = a + 1

print('Fim do programa!')