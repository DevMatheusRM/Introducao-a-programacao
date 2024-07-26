#Contagem Regressiva: Imagine que você está no centro de controle de lançamento de um foguete.
#Sua tarefa é simular a contagem regressiva, começando em 10 e indo até 0, exibindo cada número no
#console. Ao final da contagem, exiba a mensagem "Fogo!
from time import sleep

for c in range(10, 0, -1):
    print(f'Faltam {c} segundos para o lançamento!!')
    sleep(0.5)

print('FOGO!')