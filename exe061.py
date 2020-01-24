print('Gerador de PA')
print('-=-'*10)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{}... '.format(termo), end='')
    termo = termo+ razao
    cont +=1
print('FIM')