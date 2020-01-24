'''Exercício Python 072: Crie um programa que tenha uma dupla
totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

# lanche = ('Hamburguer', 'Suco', 'pizza', 'pudim')
# op 1
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')

#  op 2
# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# op 3
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição{pos}')
# print('Comi pra caramba')
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
                break
        print('Tente Novamente...', end='')
print(f'Voce digitou o numero {cont[num]}')