# cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
# cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
# print("O valor da Hipotenusa é igual à: {:.2f}".format(hipotenusa))

 # ou

import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(co, ca)
print("O valor da Hipotenusa é igual à: {:.2f}".format(hipotenusa))