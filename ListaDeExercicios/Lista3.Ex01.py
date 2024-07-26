#Contagem Regressiva: Imagine que você está no centro de controle de lançamento de um foguete. Sua tarefa é simular a
#contagem regressiva, começando em 10 e indo até 0, exibindo cada número no console. Ao final da contagem, exiba
#a mensagem "Fogo!
from time import sleep

#for x in range(10, 0, -1):
#    print(f'Faltam {x} para decolagem!')
#    sleep(1)

#print('FOGO')

contagem = 10

while contagem >= 0:
    print(f'Contagem regressiva: {contagem}')
    contagem = contagem -1
    sleep(1)

print('Fim da contagem regressiva!')
print('Fogo!!!')