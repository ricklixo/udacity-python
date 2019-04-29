# Programa que remova os numeros contidos em um arquivo qualquer e renomeie-o
# 1 - Pegar os nomes dos arquivos contidos em uma pasta
# 2 - Para cada arquivo, renomeá-lo

from os import listdir
import os

# MINHA SOLUÇÃO: 
def renomear():
    lista_arquivos = listdir('c:/dev/udacity-python/prank') #cria uma lista com o conteúdo do diretório especificado.
    print(os.getcwd) # imprime na tela o diretório de trabalho atual.
    for nome_arquivo in lista_arquivos:
        print('Nome antigo: {}'.format(nome_arquivo)) # imprime na tela o conteúdo armazenado na lista. 
        print('Nome atual: {}'.format(nome_arquivo.strip('0123456789').replace(' ', ''))) # imprime os nomes com os números removidos e também os espaços
        novo_arquivo = nome_arquivo.strip('0123456789').replace(' ', '') # atribui a variável NOVO_ARQUIVO as instruções de remover os números e espaços
        os.chdir('c:/dev/udacity-python/prank') # Muda o diretório atual para o qual os arquivos estão armazenados.
        os.rename(nome_arquivo, novo_arquivo) # renomeia os arquivos dentro da lista.
    return

renomear()