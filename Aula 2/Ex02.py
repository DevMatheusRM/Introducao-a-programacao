#Precisamos de um programa de computador que calcule a quantidade de latas de tinta e o custo total para pintar tanques
#cilíndricos de combustível.
#Sabemos que: A lata de tinta custa R$ 50,00 ; Cada lata contém 5 litros ; Cada litro de tinta pinta 3 metros quadrados
import math

print('Calculadora de quantidade de latas de tintas/custo total para pintar tanques de combustível:')
R = float(input('Dê o raio do cilíndro de combustível:'))
H = float(input('Dê a altura do cilindro de combustível:'))
Pi = math.pi

area_lateral = (2*Pi*R*H)
area_da_base = Pi*(R**2)
area_do_cilindro = (area_da_base + area_lateral)
quantidade_total_de_litros = (area_do_cilindro / 3)
quantidade_de_latas = math.ceil(quantidade_total_de_litros / 5)  # Arredonda para cima a quantidade de latas
custo = quantidade_de_latas * 50

print(f'\nÁrea total a ser pintada: {area_do_cilindro:.2f} metros quadrados')
print(f'Quantidade de tinta necessária: {quantidade_total_de_litros:.2f} litros')
print(f'Número de latas de tinta necessárias: {quantidade_de_latas}')
print(f'Custo total das latas de tinta: R$ {custo:.2f}')
