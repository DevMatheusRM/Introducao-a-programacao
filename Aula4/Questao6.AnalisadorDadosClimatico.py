#Imagine que você é um cientista de dados trabalhando em um projeto para analisar dados climáticos de
#diferentes cidades.
#Você precisa criar um conjunto de funções em Python para auxiliar na análise desses dados.
#Crie as seguintes funções:
#temperatura_media(temperaturas): Recebe uma lista de temperaturas (em graus Celsius)
# e retorna a temperatura média.temperatura_maxima(temperaturas): Recebe uma lista de temperaturas (em graus Celsius)
# e retorna a temperatura máxima.

temperaturas = [23, 24, 25, 26, 28]

def temperatura_media(temperaturas):
    soma = sum(temperaturas)
    media = soma / len(temperaturas)
    return media