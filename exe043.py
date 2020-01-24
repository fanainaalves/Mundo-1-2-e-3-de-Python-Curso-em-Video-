peso = float(input("Digite o seu peso: Kg "))
altura = float(input("Digite a sua altura: Cm "))
imc = peso / altura **2
if imc < 18.5:
    print("Seu IMC equivale à {:.2f}, ou seja você está ABAIXO do Peso!!!".format(imc))
elif imc <= 25:
    print("Seu IMC equivale à {:.2f}, ou seja você está com Peso IDEAL! Parabéns!!!".format(imc))
elif imc <= 30:
    print("Seu IMC equivale à {:.2f}, ou seja você está com SOBREPESO! Requer Cuidado!".format(imc))
elif imc <= 40:
    print("Seu IMC equivale à {:.2f}, ou seja você está com OBESIDADE! Requer Atenção".format(imc))
elif imc > 40:
    print("Seu IMC equivale à {}, ou seja você está com OBESIDADE MÓRBIDA!!! Nescessita de Atenção Com Urgencia!!!".format(imc))
else:
    print("ERRO!!!")