soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
    cont += 1
print("Voce informou {} numeros, a soma dos numeros pares é: {}".format(cont, soma))