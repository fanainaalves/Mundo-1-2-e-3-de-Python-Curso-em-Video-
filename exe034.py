salario = float(input("Digite o valor do seu salário para calcular o aumento: "))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print("Quem ganhava:R${}, agora irá ganhar:R${}". format(salario, aumento))
