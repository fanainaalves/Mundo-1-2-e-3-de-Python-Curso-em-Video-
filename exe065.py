resp = 'S'
soma = quantidade = media = 0
while resp in 'Ss':
    num = int(input("Digite um numero: "))
    soma += num
    quantidade += 1
    if quantidade ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print("Voce digitou {} numeros e a media foi {}.".format(quantidade, media))
print('O maior numero digitado foi: {}, e o menor numero digitado foi: {}.'.format(maior, menor))