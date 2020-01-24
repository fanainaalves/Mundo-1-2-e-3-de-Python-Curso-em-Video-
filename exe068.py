from random import randint
venceu = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador}\nO computador jogou {computador}.\nTotal de {total} partidas')
    print('Deu PAR' if total % 2 == 0 else print('Deu Ímpar'))
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            venceu += 1
        else:
            print('Voce Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceu!')
            venceu += 1
        else:
            print('Voce Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over!!!\nVoce Venceu {venceu} vezes!')