nome = str(input("Digite uma frase: ")).upper().strip()
print("analisando a frase, a letra A aparece {} vezes".format(nome.count("A")))
print("A primeira letra A aparece na {}ª posição.".format(nome.find("A") + 1))
print("A ultima letra A aparece na {}ª posição.".format(nome.rfind("A") + 1))
