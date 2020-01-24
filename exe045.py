from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("****************Suas Opções****************\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura")
jogador = int(input("Digite sua Jogada: "))
print('JO')
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print('-_-' * 10)
print("O computador Jogou {}".format(itens[computador]))
print("O Jogador Jogou {}".format(itens[jogador]))
print('-_-' * 10)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada INVÁLIDA!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada INVÁLIDA!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada INVÁLIDA!")
else:
    print("Jogada INVÁLIDA!")