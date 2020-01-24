def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um numero inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu nao digitar esse numero.\33[m')
            return  0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um numero inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu nao digitar esse numero.\33[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')