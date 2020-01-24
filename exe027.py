nome = str(input("Digite o seu nome completo: ")).strip()
n = nome.split()
print("O primeiro nome digitado foi: {}".format(n[0]))
print("e o ultimo nome foi: {}".format(n[len(n)-1]))