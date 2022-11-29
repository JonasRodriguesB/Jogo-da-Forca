"""LISTA COM PALAVRAS USADAS NO 'JOGO DA FORCA'"""

import random

arquivo = open('lista_de_palavras.txt', 'r')
texto = arquivo.read()
palavras = list(texto.split())


def selecionar_palavra():
    '''SELECIONA UMA PALAVRA ALEATÓRIA DE UMA LISTA DE PALAVRAS'''

    return random.choice(palavras)


def forca(erros):
    '''APENAS FAZ O DESENHO'''
    if erros == 0:
        print('     +---+ ')
        print('     |   | ')
        print('     |     ')
        print('     |     ')
        print('    _|_    ')
    elif erros == 1:
        print('     +---+ ')
        print('     |   | ')
        print('     |   O ')
        print('     |   | ')
        print('    _|_    ')
    elif erros == 2:
        print('     +---+ ')
        print('     |   | ')
        print('     |   O ')
        print('     |  /| ')
        print('    _|_    ')
    elif erros == 3:
        print('     +---+ ')
        print('     |   | ')
        print('     |   O ')
        print('     |  /|\\')
        print('    _|_    ')
    elif erros == 4:
        print('     +---+ ')
        print('     |   | ')
        print('     |   O ')
        print('     |  /|\\')
        print('    _|_ /   ')
    else:
        print('     +---+ ')
        print('     |   | ')
        print('     |   O ')
        print('     |  /|\\')
        print('    _|_ / \ ')


