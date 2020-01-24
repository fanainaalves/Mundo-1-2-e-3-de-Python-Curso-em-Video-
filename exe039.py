from datetime import date
ano = date.today().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = ano - nascimento
print("Quem nasceu em {}, tem {} anos no ano atual de {}.".format(nascimento, idade, ano))
if idade < 18:
    saldo = 18 - idade
    print("Ainda deve se alistar ao serviço militar, em {} ano(s)!".format(saldo))
    anoFaltam = saldo + ano
    print("Seu alistamento será no ano de {}".format(anoFaltam))
elif idade == 18:
    print("Já é hora de se alistar ao serviço militar!")
else:
    saldo = idade - 18
    print("Já deveria ter se alistado ao serviço militar há {} ano(s)!".format(saldo))
    anoFaltam = ano - saldo
    print("Seu alistamento era pra ter sido no ano de {}".format(anoFaltam))
