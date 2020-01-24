distancia = float(input("Digite a distancia da viagem em km's: "))
if distancia <= 200:
    multiplique = distancia * 0.50
    print("O preço a pagar é: R$ {}.".format(multiplique))
elif distancia >= 200:
    aumento_de_taxa = distancia * 0.45
    print("O valor a ser pago será de: R$ {}.".format(aumento_de_taxa))
else:
    print("erro")