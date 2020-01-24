valor_da_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
trintaPorCento = salario * 30/100
print(trintaPorCento)
quantos_anos = int(input("Digite em quantos anos você quer financiar: "))
prestacao = valor_da_casa / (quantos_anos * 12)
print("para pagar uma casa de R$ {}, em {} anos, a prestação será de R$ {}.".format(valor_da_casa, quantos_anos, prestacao))
if prestacao <= trintaPorCento:
    print("Empréstimo pode ser concedido!!!")
else:
    print("Empréstimo negado!!!")
