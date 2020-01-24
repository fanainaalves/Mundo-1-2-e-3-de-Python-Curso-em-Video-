from random import randint
from time import sleep
computador = randint(0, 5)
print("Vou pensar em um numero entre 0 e 5...")
jogador = int(input("Em que numero eu pensei?..."))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabens!!! Voce conseguiu me vencer!!")
else:
    print("Eu ganhei!!! Pensei no numero {}, e não no numero {}.".format(computador, jogador))