sexo = str(input("Digite seu sexo [F/M]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos")).strip().upper()[0]
print("Sexo {} Registrado com sucesso!".format(sexo))
