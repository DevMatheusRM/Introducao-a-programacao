#Imagine que você está trabalhando em um laboratório secreto de matemática.
#Você recebeu um conjunto de 10 números codificados (vetor A) e um número chave (X).
#Sua missão é decifrar o código multiplicando cada número do conjunto pelo número chave e armazenando os
#resultados em um novo conjunto (vetor M).
#Crie um algoritmo que:
#Leia 10 números e armazene-os no vetor A. Leia um número e armazene-o na variável X.
#Multiplique cada elemento do vetor A pelo valor de X e armazene os resultados no vetor M.
#Imprima todos os elementos do vetor M, revelando o código decifrado.

vetor_a = []
variavel_x = []
calculo = 0

for c in range(1, 11):
    pergunta = int(input('Digite um valor:'))
    vetor_a.append(pergunta)

pergunta2 = int(input('Digite agora o valor para multiplicação:'))
variavel_x.append(pergunta2)

for d in (len(vetor_a)):
    calculo = d * variavel_x

print(vetor_a)
print(variavel_x)
print(calculo)

