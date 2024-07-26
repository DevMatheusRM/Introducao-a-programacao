#Calculadora Simples: Crie uma calculadora que receba dois números e uma operação (+, -, *, /) como entrada do usuário.
#Utilize match-case para realizar a operação correspondente e exibir o resultado

numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
operacao = input('Digite a operação (+, -, *, /):')

match operacao:
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        if numero2 != 0:
            resultado = numero1/numero2
        else:
            resultado = 'Divisão por zero não é permitida!'
    case _:
        resultado = 'Operação inválida!'
print(f'O resultado: {resultado}')