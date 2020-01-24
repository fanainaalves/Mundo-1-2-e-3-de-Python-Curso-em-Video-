n1 = int(input("Primeiro numero:"))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero: "))
menor = n1
if n2 < n1 and n1 < n3:
    menor  = n2
elif n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n1 > n3:
    maior  = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print("O menor numero digitado foi: {}.\nE o maior numero digitado foi: {}.".format(menor, maior))

