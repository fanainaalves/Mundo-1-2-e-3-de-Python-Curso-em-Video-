from datetime import date
ano = int(input("Qual ano voce quer verificar? Coloque o 0 para verificar o ano atual: "))
if ano == 0:
    ano = date.today().year
elif ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!". format(ano))

else:
    print("O ano {} NÃO é BISSEXTO!".format(ano))