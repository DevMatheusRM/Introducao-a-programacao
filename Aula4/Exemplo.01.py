from datetime import datetime


#Obtém a data e hora atuais
agora = datetime.now()

#Formata a data e hora em uma string legível
data_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)