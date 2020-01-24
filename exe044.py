preço = float(input("Digite o valor do produto: R$ "))
print("[1] - À Vista (Dinheiro/Cheque): 10% de Desconto: ")
print("[2] - À Vista no cartão: 5% de Desconto ")
print("[3] - Em até 2x no cartão: Preço Formal ")
print("[4] - 3x Ou mais no cartão: 20% de Juros")
opcao = int(input("Digite o numero referente a opção desejada: "))

if opcao == 1:
    desconto10 = preço - (preço * 10 / 100)
    print("O valor do produto é igual à: R$ {}, com o desconto de 10% fica por: R$ {}.".format(preço, desconto10))
elif opcao == 2:
    desconto5 = preço - (preço * 5 / 100)
    print("O valor do produto é igual à: R$ {}, com o desconto de 10% fica por: R$ {}.".format(preço, desconto5))
elif opcao == 3:
    total = preço / 2
    print("O valor do produto em 2x será igual à: R$ {:.2f}.".format(total))
elif opcao == 4:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    print("[3] - 3x Parcelamentos")
    print("[3] - 3x ou mais Parcelas")
    juros = preço + (preço * 20 / 100)
    parcelamento = juros / parcelas
    print("O valor do produto é igual à: R$ {}, \nCom os juros de 20% fica por: R$ {}, \nDividido em {} Parcelas fica no valor de: R$ {:.2f}.".format(preço, juros, parcelas, parcelamento))
else:
    print("Valor informado está incorreto, tente novamente!")
