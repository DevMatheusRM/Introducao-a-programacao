#[FORBELLONE, 2022] O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saúde para indicar
#a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de
#um adulto e mostre sua condição.
#IMC em adultos Condição
#abaixo de 18,5 abaixo do peso
#entre 18,5 e 25 peso normal
#entre 25 e 30 acima do peso
#acima de 30 obeso

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def determinar_condicao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Acima do peso"
    else:
        return "Obeso"

# Entrada de dados pelo usuário
peso = float(input("Informe o seu peso (em kg): "))
altura = float(input("Informe a sua altura (em metros): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Determinação da condição
condicao = determinar_condicao(imc)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Condição: {condicao}")
