soma = count = 0
while True:
    num = int(input("Digite um numero [999 para parar]: "))
    if num == 999:
        break
    count += 1
    soma = soma + num
print(f'Voce digitou {count} números, a soma entre eles é igual à: {soma}.')
print('FIM')