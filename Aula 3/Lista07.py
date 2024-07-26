#Contagem de Caracteres: Imagine que você está analisando um texto e precisa saber quantas vezes cada letra aparece. Crie
#um programa que receba um texto como entrada e conte a frequência de cada letra, tanto maiúsculas quanto minúsculas.
#(Dica: pesquisa sobre o método isalpha())

texto = input("Digite um texto: ")
contagem = {}

for letra in texto:
    if letra.isalpha():
        letra = letra.lower()
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

for letra, quantidade in contagem.items():
    print(f"A letra '{letra}' aparece {quantidade} vezes.")