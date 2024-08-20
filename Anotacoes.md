| Tempos de Execução de leitura|
- 1.000 registros = 0.09 segundos
- 10.000 registros = 0.96 segundos
- 100.000 registros = 9.73 segundos
- 1.000.000 = 93.59 segundos



- Pegar razao entre onde o mês inicia e onde ele termina





"""
for prefix, event, value in ijson.parse(f):
    if prefix == 'item.month':
        print("--------------------------")
        # Atribuindo o valor à variavel
        month = value
        print("Mês : " + str(month))
    elif prefix == 'item.log':
        log = value
        print("Log: " + str(log))
    elif prefix == 'item.msg':
        msg = value
        print("Mensagem: " + str(msg))
    elif prefix == 'item.user':
        user = value
        countUser+=1
        print("User: " + str(user))
    #Parando a leitura quando atingir 100 registros
    if countUser == 2000000:
        break

"""