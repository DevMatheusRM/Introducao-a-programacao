#Jogo de adivinhação: Desafie suas habilidades de adivinhação! O computador pensou em um número entre 1 e 100,
#e sua missão é descobrir qual é. A cada tentativa, o computador dirá se o número que você chutou é maior ou menor do
#que o número secreto. Continue tentando até acertar!

from random import randint

numero_aleatorio = randint(1, 100)
Tentativa = True

while Tentativa:

    chute = int(input('Digite um número entre 1 e 100:'))

    if chute <1 or chute > 100:
        print('O valor não é valor válido!')
    elif chute == numero_aleatorio:
        print('Você acertou!')
        Tentativa = False
    elif chute < numero_aleatorio:
        print('O número tentado é MENOR do que número SEGREDO!')
    else:
        print('O número tentado é MAIOR do que número SEGREDO!')
