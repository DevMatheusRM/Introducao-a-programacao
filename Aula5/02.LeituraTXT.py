filename = 'arquivo.txt'

with open(filename, 'r', encoding='utf-8') as file_object: #'file_object' pode ser um nome qualquer. 'r' = Leitura

    '''conteudo = file_object.read() #Lê todo o arquivo de uma vez só
    print(file_object)
    print(conteudo)'''

    '''for linha in file_object: #Imprimir as linhas sem espaço
        print(linha.rstrip())'''

    '''linhas = file_object.readlines() #Imprimir apenas uma linha da lista
    for linha in linhas:
        print(f'Tipo: {type(linha)} - Texto: {linha.rstrip()})'''



