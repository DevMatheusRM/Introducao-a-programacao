from random import randint  # Importa a função randint do módulo random para gerar números aleatórios

vetor_a = []  # Inicializa uma lista vazia que representará o vetor A

# Preenche o vetor A com 10 números aleatórios entre 10 e 30
for i in range(10):
    vetor_a.append(randint(10, 30))

# Solicita ao usuário que insira um número secreto
x = int(input('Digite o número secreto: '))

vetor_multiplicador = []  # Inicializa uma lista vazia que representará o vetor multiplicador

# Multiplica cada elemento do vetor A pelo número secreto e armazena o resultado no vetor multiplicador
for i in range(len(vetor_a)):
    resultado = vetor_a[i] * x  # Calcula o resultado da multiplicação
    vetor_multiplicador.append(resultado)  # Adiciona o resultado ao vetor multiplicador

# Imprime o vetor A
print(vetor_a)
# Imprime o vetor multiplicador
print(vetor_multiplicador)
# Imprime o número secreto (multiplicador)
print(f'Multiplicador: {x}')
