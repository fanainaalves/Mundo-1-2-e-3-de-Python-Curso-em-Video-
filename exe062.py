print('Gerador de PA')
print('-=-'*10)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}... '.format(termo), end='')
        termo = termo+ razao
        cont += 1
    print('...PAUSA...')
    mais = int(input('Quantos termos voce quer mostrar a seguir? '))
print('Progressão finalizada com {} Termos.'.format(total))
print('FIM')
