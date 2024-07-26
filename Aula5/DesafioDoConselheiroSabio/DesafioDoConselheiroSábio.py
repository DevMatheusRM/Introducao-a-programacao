import json
import requests
from loguru import logger
from time import sleep

URL = 'https://api.adviceslip.com/advice'
ARQUIVO = 'lista_conselhos.txt'

def consulta_conselho(i:int) -> str:
    resposta = requests.request('GET',URL) #print(resposta.status_code) #Se sair 200 é pq está ok! (é positivo)
    mensagem = json.loads(resposta.text) #A função json.loads() em Python é usada para desserializar (ou decodificar)
    #uma string JSON, convertendo-a de volta em um objeto Python (geralmente um dicionário ou uma lista).
    #print(type(mensagem))
    conselho = mensagem['slip']['advice']

    logger.info(f'Conselho {i} consultado com sucesso!')

    return conselho + '\n'


def salvar_conselhos(lista_conselhos:list): #Função descritiva para dev.
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(lista_conselhos)

    logger.info('Lista de conselho registrada com sucesso!')


if __name__ == '__main__':

    #Armazenar conselhos
    conselhos = []

    for i in range(10):
        conselho = consulta_conselho(i + 1)
        sleep(1)

    salvar_conselhos(conselhos)