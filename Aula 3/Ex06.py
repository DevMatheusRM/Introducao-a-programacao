#Variável de controle (laço condicional)
import time

spam = 0
while spam < 5:
    print(f'Ciclo {spam} - > Hello, World.')
    spam = spam + 1 #Ao retirar o incremento, será sempre infinito
    time.sleep(1)

x = 1

while x <= 10:
    print(x)