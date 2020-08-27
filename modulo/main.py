'''
MÓDULO/PACOTE: módulo principal [main]
inGaia - Back-end Developer (Python 3.8)
Autor: José Eduardo Ceda
'''


from uteis import owm # Importa o pacote [owm]
from uteis import spotify # Importa o pacote [spotify]
from uteis.arquivo import * # Importa o pacote [arquivo]


arq = 'estatist_cidade.txt' # Nome do arquivo gerado.

if not arquivoExistente(arq): # Verifica se o arquivo não foi gerado.
    criarArquivo(arq) # Cria novo arquivo

while True:
    resposta = menu(['[CONSULTAR CIDADE]','[ESTATÍSTICA DAS CIDADES PESQUISADAS]', '[SAIR DO SISTEMAS]']) # Gera o menu de opções.
    if resposta == 1:
        cidade = input('Digite a Cidade: ')
        print(owm.tempo(cidade)) # Imprime a API contido no pacote [uteis.owm].
        print(spotify.musica()) # Imprime a API contido no pacote [uteis.spotify].
        cadastrar(arq, cidade) # Cadastra as cidades consultadas no arquivo gerado "estatist_cidade.txt".
    elif resposta == 2:
        lerArquivo(arq) # Lista as cidadaes consultadas.
    elif resposta == 3:
        print('Saindo do Sistema') # Sai do sistema.
        apagarArquivo(arq) # Apagar o arquivo "estatist_cidade.txt" para não gerar log.
        break
    else:
        print('ERRO! Digite uma opção válida!') # Caso digitado alguma opção que não contém no menu, é exibido a mensagem.