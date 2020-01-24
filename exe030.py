numero = int(input("Me diga um número qualquer: "))
resultado = numero % 2
# print("O resultado foi: {}.".format(resultado)) uma das maneiras de fazer
if resultado == 0:
    print("O numero {} é par!".format(numero))
else:
    print("O numero {} é ímpar!". format(numero))
