seg1 = int(input("Primeiro Segmento: "))
seg2 = int(input("Segundo Segmento: "))
seg3 = int(input("Terceiro Segmento: "))
if seg1 != seg2 != seg3:
    print("O Triangulo é ESCALENO!")
elif seg1 == seg2 != seg3 or seg1 != seg2 == seg3 or seg1 == seg3 != seg2 :
    print("O Triangulo é ISÓSCELES!")
elif seg1 == seg2 == seg3:
    print("O Triangulo é EQUILÁTERO!")
else:
    print("O valor informado nao forma um triangulo!")