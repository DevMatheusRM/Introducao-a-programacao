#um programa que permita saber qual o peso ideal de uma pessoa.
# para homens: (72,7 * h) -  58
# para mulheres: (62,1 * h) -  44,7
# dados de entrada: altura e sexo de uma pessoa
from time import sleep
print('Iniciando o programa...')
sleep(2)

print('Escreva aqui a sua altura e seu sexo e lhe darei o peso ideal para você!')
genero = str(input('Digite o seu gênero (M/F):')).upper()

if genero == 'M' or genero == 'F':

    altura = float(input('Digite aqui a sua altura em cm (ex: 1.22):'))
    peso_ideal = -1

    if genero == 'M':
        peso_ideal = (72.7 * altura)- 58
        genero = 'Masculino'
    elif genero == 'F':
        peso_ideal = (62.1 * altura) - 44.7
        genero = 'Feminino'

    print(f'Para um altura de {altura} cm,\n e um gênero de {genero},\n o seu peso ideal é de: {peso_ideal} kgs.')

else:
    print('Gênero inválido!')

print('----Fim do programa----')
