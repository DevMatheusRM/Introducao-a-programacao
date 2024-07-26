import json  # Importa o módulo json para trabalhar com arquivos JSON

# Nome do arquivo onde os dados serão salvos
filename = 'meu_arquivo.json'

# Dicionário contendo os dados a serem salvos no arquivo JSON
dados = {
    'nome': 'Messias',
    'idade': 38,
    'Cidade': 'João Pessoa'
}

# Abre o arquivo no modo de escrita ('w') e com codificação 'utf-8'
with open(filename, 'w', encoding='utf-8') as arquivo:
    # Usa a função json.dump() para escrever o dicionário 'dados' no arquivo
    # ensure_ascii=False é usado para garantir que caracteres não-ASCII sejam corretamente representados
    json.dump(dados, arquivo, ensure_ascii=False)

#CARREGAR (LER) UM ARQUIVO JSON
with open(filename, 'r', encoding='utf-8') as arquivo:
    dict_json = json.load(arquivo)

print(dict_json)