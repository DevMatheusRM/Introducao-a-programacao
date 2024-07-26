#Jogo de adivinhação: Desafie suas habilidades de adivinhação! O computador pensou em um número
#entre 1 e 100, e sua missão é descobrir qual é. A cada tentativa, o computador dirá se o número que
#você chutou é maior ou menor do que o número secreto. Continue tentando até acertar!
from random import randint
sorteio = randint(1, 100)

while True:
    valor_humano = int(input('O computador pensou em um valor! \n'
                             'Tente advinhar um número entre 1 e 100:'))
    valor_pc = sorteio
    print(valor_pc)
    if valor_humano > valor_pc:
        print('-' * 40)
        print(f'O valor que você deu {valor_humano} é MAIOR que o valor sorteado.\n'
              'Tente novamente!')
        print('-' * 40)
    elif valor_humano < valor_pc:
        print('-' * 40)
        print(f'O valor que você deu {valor_humano} é MENOR que o valor sorteado.\n'
              'Tente novamente!')
        print('-'*40)
    elif valor_humano == valor_pc:
        print('-' * 40)
        print('Você acertou!')
        print('-' * 40)
        break
    else:
        print('Erro')