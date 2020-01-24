soma = 0
for n in range(1, 500):
    if n % 3 == 0:
        soma = soma + n
print("A soma de todos os valores multiplos de 3, de 0 à 500 é igual à: {}.".format(soma))