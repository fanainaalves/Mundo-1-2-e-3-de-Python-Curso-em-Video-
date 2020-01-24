print('-'*40)
print('Controle de Terrenos')
print('-'*40)


def calculo_area(largura, altura):
    area = largura * altura
    print(f'A área do terreno de {largura} x {altura} é de {area} m².')


largura = float(input("Digite a LARGURA (m) do terreno: "))
altura = float(input("Digite a ALTURA (m) do terreno: "))
calculo_area(largura, altura)
