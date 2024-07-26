#Imagine que você é um alquimista numérico, capaz de manipular números como se fossem ingredientes mágicos.
#Você possui dois frascos (vetores A e B) contendo números especiais.
#Sua missão é criar uma nova poção numérica (vetor N) misturando os números de cada frasco, gota a gota.
#Crie um algoritmo que:
#Leia os números para os frascos A e B (cada frasco terá a mesma quantidade de gotas).
#Combine as gotas de A e B, uma a uma, na mesma ordem, e armazene os resultados no frasco N.
#Por exemplo, a primeira gota de N será a soma da primeira gota de A
#com a primeira gota de B. Imprima todos os números do frasco N, revelando a
#fórmula mágica da sua nova poção numérica.

from random import randint

import pygame

acumulador = []

for c in range (11):
    vetor_a =  randint(100, 500)
    vetor_b = randint(500,999)
    acumulador.append((vetor_a and vetor_b))
    print(f'A {c}º gota do frasco N é igual é a junção da gota A ({vetor_a}) e gota B ({vetor_b})')

print(f'Segue a fórmula mágica -> {acumulador}')


