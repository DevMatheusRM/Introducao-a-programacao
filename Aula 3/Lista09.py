#Soma dos Pares: Dada uma lista de números, você precisa calcular
#a soma de todos os números pares presentes nela. Crie
#um programa que realize essa tarefa de forma automática.

numeros = [5, 8, 2, 10, 1]  # Exemplo de lista
soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos números pares é: {soma_pares}")