km_percorrido = float(input("Digite a quantidade de KM percorridos durante o trajeto: "))
dias_aluguel = float(input("Digite por quantos dias o carro foi alugado: "))
preço = (km_percorrido * 0.15) + (dias_aluguel * 60)
print("A quantidade de dias alugados foram {}, a quantidade de Km rodados foram {}, o Total a pagar será: {}.".format(dias_aluguel, km_percorrido, preço))