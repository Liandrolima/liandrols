from time import sleep
from confg import matricInt, linha, cabeçalho

def menu(lista):
    sleep(2)
    cabeçalho('          \033[30;42mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = matricInt('\033[36mSua opção: \033[m')
    return opc
