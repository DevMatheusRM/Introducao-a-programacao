try:
    print (50 / 0)

except ZeroDivisionError as error:
    print(f'Erro de divisão por zero: {error}')
finally:
    print('Recurso opcional!')


'''except Exception as error: #'as' significa apelido, e posso colocar o nome que preferir.
    print(error)
    print('Tentar mais uma vez')'''