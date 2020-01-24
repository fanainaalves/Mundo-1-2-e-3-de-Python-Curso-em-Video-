num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
if num1 > num2:
    print("O numero {} é maior que o numero {}.".format(num1, num2))
elif num1 < num2:
    print("O numero {} é maior que o numero {}.".format(num2, num1))
elif num1 == num2:
    print("Os Numeros {} e {} são iguais!".format(num1, num2))
else:
    print("Não encontrado!")