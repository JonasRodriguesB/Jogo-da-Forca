'''JOGO DA FORCA'''

from palavras import *
from time import sleep

palavra = selecionar_palavra()
palavra_oculta = ['_'] * len(palavra)
letras_usadas = []
erros = 0
pontuacao = 0
continuar = True

# Apresentação e diálogo inicial
print('Bem-vindo(a) ao Jogo da Forca')
sleep(1)
print('Selecionamos uma palavra e seu desafio é adivinhá-la')
sleep(2)
print('Você pode errar no máximo 5 vezes')
sleep(2)
print('Boa sorte!')
sleep(1)


# Jogo começa
while continuar:
    forca(0)
    x = ''.join(palavra_oculta)
    print(f'PALAVRA: {x}')
    while palavra_oculta.count('_') > 0:
        letra = input(str('Insira uma letra para começar: ')).upper()
        while letra in letras_usadas or len(letra) != 1:
            letra = input(str('Insira uma letra para começar: ')).upper()
        sleep(1)
        if letra in palavra:
            letras_usadas.append(letra)
            letras_usadas.sort()
            print(f'A palavra contém a letra {letra}, parabéns!')
            sleep(1)
            encontros = palavra.count(letra)
            if encontros == 1:
                idx = palavra.find(letra)
                palavra_oculta[idx] = letra
            else:
                for n, i in enumerate(palavra):
                    if i == letra:
                        palavra_oculta[n] = letra
            x = ''.join(palavra_oculta)
            forca(erros)
            sleep(1)
            print(f'PALAVRA: {x}')
            print(f'Letras Usadas: {letras_usadas}')
            print(f'Erros = {erros}')
        else:
            print(f'A palavra não contém a letra {letra}')
            sleep(1)
            print('Tente novamente')
            erros += 1
            forca(erros)
            letras_usadas.append(letra)
            letras_usadas.sort()
            sleep(1)
            print(f'PALAVRA: {x}')
            print(f'Letras Usadas: {letras_usadas}')
            print(f'Erros = {erros}')
        if erros == 5:
            break
    if erros == 5:
        print(f'Que pena, você perdeu!')
        pontuacao = 0
    else:
        print(f'Parabéns, você concluiu o desafio')
        pontuacao += 1
        if pontuacao == 1:
            print(f'Você marcou +1 ponto e está com {pontuacao} vitória consecutiva')
        else:
            print(f'Você marcou +1 ponto e está com {pontuacao} vitórias consecutivas')
    print(f'A palavra era: {palavra}')
    selec_cont = input('Gostaria de continuar? ')
    if selec_cont:
        continuar = True
        palavra = selecionar_palavra()
        palavra_oculta = ['_'] * len(palavra)
        letras_usadas = []
        erros = 0
        print('Selecionamos uma nova palavra para você')
        sleep(1)
    else:
        continuar = False
        print('Obrigado, volte sempre!')