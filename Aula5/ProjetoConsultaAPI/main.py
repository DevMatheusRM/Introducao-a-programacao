'''Faça uma requisição à API https://api.adviceslip.com/advice para obter um conselho aleatório em formato JSON.
Utilize a estrutura de dicionário do Python para extrair o conselho da resposta JSON.
Exiba o conselho de forma clara e elegante para o usuário.
Ofereça ao usuário a opção de receber outro conselho ou encerrar o programa.'''

import json
import requests
from loguru import logger
from time import sleep
from deep_translator import GoogleTranslator

URL = 'https://api.adviceslip.com/advice'
ARQUIVO = 'conselhos.txt'

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


def traduzir_conselho(conselho:str) -> str:
    texto_traduzido = GoogleTranslator(source='english', target='portuguese').translate(conselho)
    logger.info('Tradução realizada com sucesso!')
    return texto_traduzido + '\n'


if __name__ == '__main__':

    #Armazenar conselhos
    conselhos = []

    for i in range(10):
        conselho = consulta_conselho(i + 1)
        conselho_trad = traduzir_conselho(conselho)
        conselhos.append(conselho_trad)
        sleep(1)

    salvar_conselhos(conselhos)