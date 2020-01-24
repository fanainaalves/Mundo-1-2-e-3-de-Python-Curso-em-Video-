galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!!! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO!!! Por favor digite apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f'A) Ao todo, temos: {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print('       ', end='')
        for keys, values in pessoa.items():
            print(f'{keys} = {values}: ', end='')
        print()
print('<<< ENCERRANDO >>>')
