n = float(input("Digite o preço do produto: R$ "))
desconto = n - (n * 5 / 100)
print("O valor do produto é igual à R$ {}, e com o desconto de 5% equivale à R$ {}".format(n, desconto))