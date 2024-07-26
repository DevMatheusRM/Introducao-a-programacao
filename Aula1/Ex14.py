#[FORBELLONE, 2022] Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética
#desejada; calcule, então, a resposta adequada.
#Utilize os símbolos da tabela a seguir para ler qual operação aritmética escolhida:  + = Adição / - = Subtração /
#* = Multiplicação / / = Divisão / ** / Potenciação

valor_1 = int (input('Digite aqui o número desejado:'))
valor_2 = int (input('Digite aqui outro número desejado:'))
simbolo_desejado = str(input('Certo. Agora escolha qual operação aritmética você deseja: \n'
                             '- "+" para adição;'
                             '- "-" para subtração;'
                             '- "*" para multiplicação;'
                             '- "/" para divisão;'
                             '- "**" para potenciação.')).strip()

if simbolo_desejado == '+':
    print(f'Você escolheu SOMA! \n'
          f'O resultado é {valor_1 + valor_2}')
elif simbolo_desejado == '-':
    print(f'Você escolheu SUBTRAÇÃO! \n'
          f'O resultado é {valor_1 - valor_2}')
elif simbolo_desejado == '*':
    print(f'Você escolheu MULTIPLICAÇÃO! \n'
          f'O resultado é {valor_1 * valor_2 :.2f}')
elif simbolo_desejado == '/':
    print(f'Você escolheu DIVISÃO \n'
          f'O resultado é {valor_1/valor_2}')
elif simbolo_desejado == '**':
    print(f'Você escolheu POTENCIAÇÃO \n'
          f'O resultado é {valor_1 ** valor_2:.2f}')