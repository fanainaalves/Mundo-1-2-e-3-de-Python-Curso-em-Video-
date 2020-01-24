from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome Completo: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['contratação']
print('-=' * 30)
for keys, values in dados.items():
    print(f'   - {keys} tem o valor {values}')