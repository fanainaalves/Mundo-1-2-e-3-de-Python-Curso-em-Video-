while True:
    valor = int(input('Digite um valor para ver a sua tabuada: '))
    if valor < 0:
        break
    print('-='*30)
    for c in range(1, 11):
        print(f'{valor}x{c} = {valor*c}')
    print('-='*30)
print('Programa ENCERRADO! \nVolte Sempre!')