'''
MÓDULO/PACOTE: arquivo
inGaia - Back-end Developer (Python 3.8)
Autor: José Eduardo Ceda
'''

# Função para número inteiro.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar.\033[m')
            return 0
        else:
            return n

# Função para gerar linha do tamanho 42.
def linha(tam = 42):
    return '-' * tam

# Função para gerar o cabeçalho.
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# Função para gerar o menu.
def menu(lista):
    cabecalho('InGaia - Back-end Developer')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mOpção: \033[m')
    return opc