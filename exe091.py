from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores Sorteados: ')
for keys, valores in jogo.items():
    print(f'{keys} tirou {valores} Pontos no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for indice, valores in enumerate(ranking):
    print(f'    {indice+1}º Lugar: {valores[0]} com {valores[1]}.')
    sleep(1)
