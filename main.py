from funcoes import *
import time


print(verificar_arquivo('data.json'))
dados = ler_arquivo('data.json')
print("------------------------")
print("Olá Forasteiro!")


# Criando as listas, separadas pelo mês ------------
cria_listas(dados)
#---------------------------------------------------

numLog = int(input("Informe o número do suspeito: "))

print("\nEncontrando o impostor...")
tempoInicial = time.time()
impostor = verifica_impostor(numLog)
tempoFinal = time.time()


if impostor:
    print("\n")
    print("< =========== IMPOSTOR ENCONTRADO =========== >\n")
    print(f"Nome: {impostor['user']}")
    print(f"Log: {impostor['log']}")
    print(f"Mês: {impostor['month']}")
    print(f"Mensagem: {impostor['msg']}")
    print("\n ----------")
    print("Tempo para encontrar o impostor: {:.2f} s".format(tempoFinal - tempoInicial))
    print("\n")
else:
    print("Impostor não encontrado....")




