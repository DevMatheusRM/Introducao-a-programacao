#Média de Notas: Ajude um professor a calcular a média das notas de seus alunos! Escreva um
#programa que permita ao professor inserir as notas de cada aluno, uma por vez. Quando o professor
#digitar -1, o programa deve calcular e exibir a média das notas inseridas.



'''while True:
    print('-'*40)
    nota_1=float(input('Digite a nota do 1º do aluno:'))
    nota_2 = float(input('Digite a nota do 2º do aluno:'))
    print('Ok.')
    print('Deseja continuar?')
    continuar = str(input('[S/N]:')).upper().strip()[0]
    if continuar == 'N':
        print(f'Ok. A média foi de {(nota_1+nota_2)/2}')
        break'''

soma_notas = 0
quantidade_notas = 0

while True:
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))
    if nota == -1:
        break
    soma_notas += nota
    quantidade_notas += 1

if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")