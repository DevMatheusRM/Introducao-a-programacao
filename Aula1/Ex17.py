#Um dicionário Python pode ser usado para modelar um dicionário de verdade.
#No entanto, para evitar confusão, chame este dicionário de glossário.

#a. Pense em cinco palavras relacionadas à programação que você conhece. Use estas palavras como chaves em seu
#glossário e armazene seus significados como valores.

#b. Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo:
#você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma
#linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
#para inserir uma linha em branco entre cada palavra-significado em sua saída.

glossario = {'Caneta':'Objeto utilizado para escrita',
             'Corretivo':'Objeto utilizado para apagar erros',
             'Papel':'Usado como ambiente de escrita',
             'Borracha':'Usado apenas para apagar erros de lápis',
             'Grampeador':'Usado para juntar papéis'}

print(f'Caneta : {glossario['Caneta']}\n'
      f'Corretivo: {glossario['Corretivo']}\n'
      f'Papel: {glossario['Papel']}\n'
      f'Borracha: {glossario['Borracha']}\n'
      f'Grampeado: {glossario['Grampeador']}')
