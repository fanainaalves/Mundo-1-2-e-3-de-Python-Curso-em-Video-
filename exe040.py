nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma = (nota1 + nota2)/2
if soma < 5.0:
    print("A primeira nota foi {}, a segunda nota foi {}. A Média é igual à {}. Aluno REPROVADO".format(nota1, nota2, soma))
elif soma > 5.0 < 6.9:
    print("A primeira nota foi {}, a segunda nota foi {}. A Média é igual à {}. Aluno em RECUPERAÇÂO".format(nota1, nota2, soma))
elif soma >= 7.0:
    print("A primeira nota foi {}, a segunda nota foi {}. A Média é igual à {}. Aluno em APROVADÍSIMO".format(nota1, nota2, soma))
else:
    print("DADOS INVÁLIDOS")