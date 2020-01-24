import math
# OPÇÃO 1:

numero = float(input("Digite um numero: "))
num_inteiro = math.trunc(numero)
print("o numero digitado foi: {}, a sua parte inteira é: {}.".format(numero,num_inteiro))
# OPÇÃO 2:

# numero = float(input("Digite um numero: "))
# num_inteiro = math.floor(numero)
# print("o numero digitado foi: {}, a sua parte inteira é: {}.".format(numero,num_inteiro))

# OPÇÃO 3: também pode ser feito com o INT, sem fazer importação da biblioteca

# numero = float(input("Digite um numero: "))
# print("o numero digitado foi: {}, a sua parte inteira é: {}.".format(numero, int(numero)))


