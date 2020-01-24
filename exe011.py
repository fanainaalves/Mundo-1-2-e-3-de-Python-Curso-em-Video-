altura = float(input("Qual o tamanho da altura da sua parede em cm? "))
largura = float(input("Qual o tamanho da largura da sua parede em cm? "))
area = altura * largura
tinta = area / 2
print("Como a sua parede equivale à: {} x {}, a Àrea da parede é igual à: {:.2f}m². \n "
      "Você vai precisar de {}L de tinta".format(altura, largura, area, tinta))