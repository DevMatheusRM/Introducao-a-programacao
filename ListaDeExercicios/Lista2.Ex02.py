#Conversor de Temperatura: Faça um programa que converta temperaturas entre Celsius e Fahrenheit.
#O usuário deve informar a temperatura e a escala de origem, e o programa deve
#calcular e exibir a temperatura na outra escala

from time import sleep
print('----Inicializando sistema----')
sleep(2)

tipo_Medidor=str(input('Digite "C" para Celsius e "F" para Fahrenheit a seguir:')).upper()
valor=float(input('Digite o valor:'))

if tipo_Medidor == "C" or 'F':
    if tipo_Medidor == 'C':
        calculo_celsius_para_fahrenheit = (valor * 1.8) + 32
        print(f'O resultado é de: {calculo_celsius_para_fahrenheit:.2f}ºF')
    elif tipo_Medidor == 'F':
        calculo_fahrenheit_para_celsius = (valor - 32) / 1.8
        print(f'O resultado é de:{calculo_fahrenheit_para_celsius:.2f}ºC ')
else:
    print(f'O tipo medidor {tipo_Medidor} é inválido.')

print('----Finalizando Sistema----')