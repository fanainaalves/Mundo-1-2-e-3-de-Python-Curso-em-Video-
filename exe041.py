from datetime import date
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(" Sua Idade é {}, você se classifica como Atleta MIRIM.".format(idade))
elif idade <= 14:
    print(" Sua Idade é {}, você se classifica como Atleta INFANTIL.".format(idade))
elif idade <= 19:
    print(" Sua Idade é {}, você se classifica como Atleta JÚNIOR.".format(idade))
elif idade <= 25:
    print(" Sua Idade é {}, você se classifica como Atleta SÊNIOR.".format(idade))
elif idade > 25:
    print(" Sua Idade é {}, você se classifica como Atleta MASTER.".format(idade))
else:
    print("Idade não encontrada!")