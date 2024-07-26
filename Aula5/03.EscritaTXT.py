filename = 'minhas_linguagens.txt'

with open(filename, 'w' , encoding='utf-8') as arquivo:
    #'arquivo' é apelido /
    #'w' = Escrita
    #'a' = Adicionar
    #Lembrar do /n para pular linha
    arquivo.write('Eu amo programar em Pyhton\n')
    arquivo.write('Eu amo programar em SQL\n')
    arquivo.write('Eu amo programar em Java\n')