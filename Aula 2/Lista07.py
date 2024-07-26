#Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital.
#O programa deve permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar
#se o saldo da conta está positivo ou negativo.
#Se negativo, informa qual o valor será necessário para quitar o débito.

print('='*40)
print('Simulador de Banco')
print('='*40)

deposito = float(input('Digite aqui o valor para depósito:'))
saque = float(input('Valor depositado! Agora, realize um saque. Digite a quantia desejada:'))

if saque == deposito:
    print('Você sacou todo o dinheiro de sua conta.')
elif saque > deposito:
    print(f'Opa! temos um problema. Você sacou um valor maior que '
          f'seu valor em caixa. (Você utilizou R$ {saque - deposito} em cheque especial!)')
elif saque < deposito:
    print(f'Valor em conta restante: {deposito - saque}')
else:
    print('Inválido, tente novamente')