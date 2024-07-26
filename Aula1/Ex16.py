#Nossa equipe de desenvolvimento ficou responsável por desenvolver um programa que gerencie uma lista de convidados
#para uma festa. É preciso criar uma mensagem padrão, e uma lista de convidados. Você pode escolher três personagens de
#filmes para adicionar a sua lista de convidados.
#a. Sabendo que um dos seus convidados não pode participar, adicione ao programa uma mensagem informando que
#ele será retirado da lista, e altere o código para receber um novo personagem. Não esqueça de utilizar as funções
#que te permite adicionar os novos convidados pelo teclado.
#b. Adicione a opção de poder adicionar mais pessoas à sua lista.
#i. Uma opção para adicionar um convidado querido ao início da lista;
#ii. Uma convidado no meio da lista;
#iii. E por um convidado ao fim da lista;

lista_de_convidados = ['Jonh Wick','Neo Anderson','Tony Stark']
print('-'*30)
print(f'Bem vindos a festa, {lista_de_convidados[0]}, {lista_de_convidados[1]}, {lista_de_convidados[2]}!')
print('-'*30)
print(f'Infelizmente fiquei sabendo que o convidado {lista_de_convidados[1]} não pode participar. '
      f'Ele será retirado da lista.')
print('-'*30)
substituir=str(input('Digite o nome do novo convidado no lugar dele:'))
lista_de_convidados[1] = substituir
print('-'*30)
print(f'Lista atualizada: {lista_de_convidados}')
print('-'*30)

adicionar_pessoas = str(input('Deseja adicionar mais pessoas a lista? [S/N]')).upper().strip()[0]
while adicionar_pessoas == 'S':
    nome_convidado_adicionado = str(input('Digite o nome do convidado(a):'))
    alternativas = int(input('Escolha aonde colocar o nome:\n'
                                 '- Início da lista: [1]\n'
                                 '- Meio da lista: [2]\n'
                                 '- Fim da lista: [3]\n'
                                 'Digite o número respectivo:'))
    if alternativas == 1:
            lista_de_convidados.insert(0,nome_convidado_adicionado)
    elif alternativas == 2:
            lista_de_convidados.insert(2,nome_convidado_adicionado)
    elif alternativas == 3:
            lista_de_convidados.append(nome_convidado_adicionado)
    print(f'Lista de convidados atualizada: {lista_de_convidados}')
    adicionar_pessoas = str(input('Deseja adicionar mais pessoas a lista? [S/N]')).upper().strip()[0]
    if adicionar_pessoas == 'N':
        print(f'Ok, segue a lista final: {lista_de_convidados}')
    break
