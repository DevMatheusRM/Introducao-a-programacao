#Imagine que você está construindo um sistema de segurança que precisa registrar eventos importantes,
#como o horário em que uma porta foi aberta ou um alarme foi acionado.

#Crie um algoritmo que: Utilize um laço de repetição infinito para simular o monitoramento contínuo do sistema.
#Dentro do laço, simule a ocorrência de eventos em intervalos de tempo aleatórios (por exemplo, a cada 1-5 segundos).
#Utilize a biblioteca datetime para obter a data e hora exatas de cada evento.
#Formate a data e hora em um formato legível (por exemplo, "12/07/2024 17:30:15").
#Imprima uma mensagem no console indicando o tipo de evento e a data/hora em que ocorreu (por exemplo,
#"Porta aberta em 12/07/2024 17:30:15").
#Este exercício simula um sistema de log básico. Em um sistema real, os logs seriam armazenados em um
#arquivo ou banco de dados para posterior análise.

from random import randint
from datetime import datetime
from time import sleep

eventos_aleatorios = ['Porta Aberta', 'Luz acesa', 'Janela Aberta']

while True:
    #Simula um intervalo de tempo aleatório entre eventos
    sleep(randint(1, 5))

    #Hora e data
    agora = datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')

    #Seleciona um evento aleatório
    evento = eventos_aleatorios[randint(0, len(eventos_aleatorios) - 1)]

    #Importa para bloco de notas
    mensagem_formatada = f'{agora} - {evento.upper()}'
    with open('eventos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(mensagem_formatada + '\n')

    print(f'{evento} em {data_formatada}')






