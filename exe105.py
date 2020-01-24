def notas(*n, sit=False):
    """-> Função para analisar notas de varios alunos.
    para n: uma ou mais notas dos alunos (aceita varias);
    para sit: valor opconal, indicando se deve ou nao adicionar a situação;
    return: dicionário com várias informações sobre a situação da turma."""

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'


resposta = notas(5.5, 2.5, 1.5, sit=True)
print(resposta)
help(notas)