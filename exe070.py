print('=-='*10)
print('      LOJA DESCONTAÇO')
print('=-='*10)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input("Digite o nome do produto: "))
    preço = float(input('Preço: R$ '))
    cont +=1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:~^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R$ {barato} que custou R${menor:.2f}')