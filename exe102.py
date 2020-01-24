def fatorial(n, show=False):
    """ -> calcula o fatorial de um numero,
    para o N: O numero a ser calculado;
    para o SHOW: (opcional) mostrar ou não a conta;
    para o RETURN: retorna o valor do fatorial de um numero (N)."""
    f =1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f += c
    return f

print(fatorial(5, show=True))
help(fatorial())