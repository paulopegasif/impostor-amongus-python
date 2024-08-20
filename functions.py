import json
import os

LOGS_JANEIRO = []
LOGS_FEVEREIRO =[]
LOGS_MARCO =[]
LOGS_ABRIL =[]
LOGS_MAIO =[]
LOGS_JUNHO =[]
LOGS_JULHO =[]
LOGS_AGOSTO =[]
LOGS_SETEMBRO =[]
LOGS_OUTUBRO =[]
LOGS_NOVEMBRO =[]
LOGS_DEZEMBRO =[]

def verificar_arquivo(arquivo):
    #Verificando se o arquivo existe no diretório
    if os.path.exists(arquivo):
        return("Arquivo encontrado!")
    else:
        return("Arquivo não encontrado!")


def ler_arquivo(arquivo):
    # abre o arquivo para leitura
    with open(arquivo) as f:
        arquivo = json.load(f)

        return (arquivo)
    

    
def mostra_tamanho(lista):
    #Mostrar o tamanho do arquivo
    return len(lista)

def obter_max_digito(lista):
    #Obter quantidade de máxima dígitos no log
    max_digitos = 0

    for obj in lista:
        log = obj.get('log')
        qtd_digito = len(str(log))

        if qtd_digito > max_digitos:
            max_digitos = qtd_digito


    return max_digitos


def cria_listas(lista):

    # Definindo o global para alterar as listas globais
    global LOGS_JANEIRO, LOGS_FEVEREIRO, LOGS_MARCO, LOGS_ABRIL, LOGS_MAIO, LOGS_JUNHO, LOGS_JULHO, LOGS_AGOSTO, LOGS_SETEMBRO, LOGS_OUTUBRO, LOGS_NOVEMBRO, LOGS_DEZEMBRO

    #Função para criar as listas
    LOGS_JANEIRO = [log for log in lista if log.get('month') == 'January']
    LOGS_FEVEREIRO = [log for log in lista if log.get('month') == 'February']
    LOGS_MARCO = [log for log in lista if log.get('month') == 'March']
    LOGS_ABRIL = [log for log in lista if log.get('month') == 'April']
    LOGS_MAIO = [log for log in lista if log.get('month') == 'May']
    LOGS_JUNHO = [log for log in lista if log.get('month') == 'June']
    LOGS_JULHO = [log for log in lista if log.get('month') == 'July']
    LOGS_AGOSTO = [log for log in lista if log.get('month') == 'August']
    LOGS_SETEMBRO = [log for log in lista if log.get('month') == 'September']
    LOGS_OUTUBRO = [log for log in lista if log.get('month') == 'October']
    LOGS_NOVEMBRO = [log for log in lista if log.get('month') == 'November']
    LOGS_DEZEMBRO = [log for log in lista if log.get('month') == 'December']






def verifica_impostor(indexLog):
    # Função para verificar o número de log informado
    global LOGS_JANEIRO, LOGS_FEVEREIRO, LOGS_MARCO, LOGS_ABRIL, LOGS_MAIO, LOGS_JUNHO, LOGS_JULHO, LOGS_AGOSTO, LOGS_SETEMBRO, LOGS_OUTUBRO, LOGS_NOVEMBRO, LOGS_DEZEMBRO

    listas = [LOGS_JANEIRO, LOGS_FEVEREIRO, LOGS_MARCO,
                LOGS_ABRIL, LOGS_MAIO, LOGS_JUNHO, LOGS_JULHO,
                LOGS_AGOSTO, LOGS_SETEMBRO, LOGS_OUTUBRO, LOGS_NOVEMBRO, LOGS_DEZEMBRO]

    tamanho_atual = 0
    posLista = 0

    try:
        while True:
            if indexLog < len(listas[posLista]) + tamanho_atual:
                listas[posLista] = radix_sort(listas[posLista])
                impostor = listas[posLista][indexLog - tamanho_atual]
                return impostor
            else:
                tamanho_atual += len(listas[posLista])
                posLista += 1
    except IndexError:
        print("O índice informado é inválido...")     



def radix_sort(lista):

    # Encontra o número máximo de dígitos nos elementos da lista
    max_digits = obter_max_digito(lista)

    #print(f"Max digits: {max_digits}")

    # Setando a base (radix) para decimal (10)
    base = 10

    # Lista armazenar os elementos com base em seus valores de dígitos
    compartimentos = [[] for _ in range(base)]

    # Itera por cada dígito, começando pelo menos significativo
    for i in range(0, max_digits):
        # Itera pelos objetos da lista
        for obj in lista:
            # Extrai o i-ésimo dígito do número de log do objeto
            digito = (obj['log'] // base ** i) % base
            # Adiciona o objeto ao compartimento correspondente ao i-ésimo dígito
            compartimentos[digito].append(obj)

        # Combina os compartimentos de volta na lista, começando com os elementos na fila 0
        lista = [obj for fila in compartimentos for obj in fila]
        # Limpa os compartimentos para a próxima iteração
        compartimentos = [[] for _ in range(base)]

    return lista



if __name__ == "__main__":
    verificar_arquivo('./data.json')
    ler_arquivo('./data.json')
