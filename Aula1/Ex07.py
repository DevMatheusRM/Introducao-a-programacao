#Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em
#km) e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado.

pergunta = float(input('Digite a distância da sua viagem em Km/h:'))
pergunta2 = float(input('Digite a velocidade média em Km/h:'))
calculo = (pergunta/pergunta2)
print(f'O tempo da viagem em  horas é {calculo:.0f} hora(s).')
