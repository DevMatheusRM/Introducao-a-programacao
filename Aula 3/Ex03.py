#Identificador nome e uma lista de nomes
frutas = ['pêra', 'uva', 'maça', 'kiwi']
print('Lista de frutas:')
print(frutas)

#Alterando o elemento que está na posição 1
frutas[1] = 'Abacate'

#Imprimir a lista
print('Lista de frutas (alterada):')
print(frutas)

#Inserir dado (função insert)
frutas.insert(2, 'morango')
print('Lista de frutas (inserido morango):')
print(frutas)

#Adicionar elementos ao final da lista
frutas.append('Pitaya')
print('Lista de frutas (inserindo Pitaya):')
print(frutas)

#Remover elemento da lista
del frutas[0]
print('Lista de frutas (removido pêra):')
print(frutas)

print('-----'*20)

#Acrescentar no último índice da lista.
frutas.append('Melancia')

if 'Melancia' in frutas:
    print(f'Índice de Melancia: {frutas.index("Melancia")}')

print('Removendo a Pitaya e a Melancia:')
frutas.remove('Pitaya')
frutas.remove('Melancia')

print('Lista de frutas (removido Pitaya e Melancia):')
print(frutas)

# pop - Removendo o elemento da lista
fruta_removida = frutas.pop(2)
print('Lista de frutas:')
print(frutas)
print(f'Fruta removida {fruta_removida}')