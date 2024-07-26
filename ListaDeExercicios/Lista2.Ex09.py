#9. [FORBELLONE, 2022] Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada;
#calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operação aritmética escolhida.

valor1=int(input('Digite um número:'))
valor2=int(input('Digite outro número:'))
operador_escolhido=int(input('Digite o número respectivo ao operador escolhido: 1 -> - \n 2 -> + \n 3 -> * \n 4 -> /'))

if operador_escolhido == 1:
    print(f"{valor1 - valor2} é o resultado")
elif operador_escolhido == 2:
    print(f'{valor1 + valor2} é o resultado}")
elif operador_escolhido == 3:
    print(f'{valor1 * valor2} é o resultado}")
elif operador_escolhido == 4:
    print(f'{valor1 / valor2} é o resultado}")
else:
    print('Valor inválido!')