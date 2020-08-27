'''
MÓDULO/PACOTE: arquivo
inGaia - Back-end Developer (Python 3.8)
Autor: José Eduardo Ceda
'''


import os # Importa a biblioteca [os] sistema operacional.
from uteis.interface import * # Importa o pacote [uteis.interface].
from collections import Counter # Importa a biblioteca [collections].

# Função para verificar se o arquivo já existe.
def arquivoExistente(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Função para criar o arquivo.
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO de criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

# Função para ler o arquivo.
def lerArquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf8')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('ESTATÍSTICA DAS CIDADES PESQUISADAS')
        with open(nome) as est:
            estatist = Counter(est.read().splitlines()) # splitlines() para não quebrar a cidade que possui dois nomes com a entrada de "enter"
            for item in estatist.items(): print("{}\t{}".format(*item)) # número de vezes que as cidades aparecem
        #print(a.read())
    finally:
        a.close()

# Função para apagar o arquivo.
def apagarArquivo(nome):
    os.remove(os.path.join(nome))

# Função para registrar.
def cadastrar(arq, nome):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('Erro ao gravar o arquivo!')
        else:
            a.close()
