#Jogo de Dados: Simule a emoção de um jogo de dados com dois jogadores!
#Crie um programa que permita que cada
#jogador jogue um dado virtual e determine o vencedor da rodada,
#ou seja, aquele que obtiver o maior número no dado.

import random

for rodada in range(1, 4):  # 3 rodadas
    print(f"\nRodada {rodada}:")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Jogador 1 tirou {dado1}")
    print(f"Jogador 2 tirou {dado2}")

    if dado1 > dado2:
        print("Jogador 1 venceu a rodada!")
    elif dado2 > dado1:
        print("Jogador 2 venceu a rodada!")
    else:
        print("Empate na rodada!")