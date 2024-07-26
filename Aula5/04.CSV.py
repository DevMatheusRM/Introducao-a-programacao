import csv

filename = 'arquivo2.csv'

with open(filename, newline='', encoding='utf-8') as arquivo:
    #'newline' é um recurso necessário para CSV, pois não e tem '\n' no CSV
    leitor = csv.reader(arquivo) #delimiter = ';') #Como delimitador é importante utilizar ";" [Para dados Brasileiro]

    #Para não mexer nos dados originais.
    leitor_limpo_caracteres = []

    for linha in leitor: #Lista iniciada vazia para cada repetição
        lista_temporaria = []

        for objeto in linha: # Percorrer cada coluna da minha linha # Limpara cada item da linha - Remover espaços em Branco
            lista_temporaria.append(objeto.strip())

    leitor_limpo_caracteres.append(lista_temporaria)

print(leitor_limpo_caracteres)