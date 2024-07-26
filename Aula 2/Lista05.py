#Verificador de Vogais: Crie um programa que verifique se uma letra (informada pelo usuário) é uma vogal ou consoante.

letra=str(input('Digite uma letra:'))

if letra in 'aeiou':
    print('É vogal.')
else:
    print('É consoante')