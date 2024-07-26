#Contador de Vogais: Você é um linguista curioso e quer saber quantas vogais existem em uma frase.
#Crie um programa que receba uma frase como entrada e conte quantas vogais (a, e, i, o, u) ela possui
'''from time import sleep

soma = 0
vogais = 'aeiou'

while True:
    frase = str(input('Digite aqui a frase:')).lower()
    if vogais in frase:
        print('Indentifiquei que nesta frase existe vogal!\n'
              'Agora direi quantas:')
        print('----Carregando----')
        sleep(2)
        if "a" in frase:
            soma += len('a', frase)
        elif 'e' in frase:
            soma += len('e', frase)
        elif 'i' in frase:
            soma += len('i', frase)
        elif 'o' in frase:
            soma += len('o', frase)
        elif 'u'in frase:
            soma += len('u', frase)
        print(f'Sua frase possui {soma} vogais!')
    else:
        print('Sua frase não possui vogais.')'''

frase = input("Digite uma frase: ").lower()
contador_vogais = 0

for letra in frase:
    if letra in "aeiou":
        contador_vogais += 1

print(f"A frase possui {contador_vogais} vogais.")