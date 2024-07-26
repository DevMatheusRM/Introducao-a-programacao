#Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital. O programa deve
#permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar se o saldo da conta está positivo ou
#negativo. Se negativo, informa qual o valor será necessário para quitar o débito.

valor_deposito=float(input('Coloque o valor para depósito: R$'))
from time import sleep
sleep (1)
print('=-=-Carregando-=-=')
sleep (1)
print (f'Certo, o valor da sua conta hoje é de R$ {valor_deposito}')
sleep (1)
valor_saque=float(input('Agora coloque o valor do saque: R$'))
sleep (1)
print('=-=-Calculando-=-=')
calculo_de_debito=(valor_saque - valor_deposito)
calculo_de_sobra=(valor_deposito - valor_saque)
if valor_saque > valor_deposito:
    print (f'Opa! Você está com saldo negativo. \n Para quitar o débito você precisa pagar o valor de R$ {calculo_de_debito}')
elif valor_deposito == valor_saque:
    print (f'Você sacou todo o seu valor. Hoje você está com a conta zerada!')
else:
    print (f'Ok. Você retirou R$ {valor_saque}, e sobrou R$ {calculo_de_sobra}.')
