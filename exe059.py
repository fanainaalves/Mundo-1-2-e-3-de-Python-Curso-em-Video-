num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
op = 0
while op != 5:
    print("[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos Números\n[5] - Sair do programa")
    op = int(input("Digite sua opção: "))
    if op == 1:
        soma = num1 + num2
        print("A soma de {} + {} equivale à: {}.".format(num1, num2, soma))
    elif op == 2:
        multiplicação = num1 * num2
        print("A multiplicação de {} * {} equivale à: {}.".format(num1, num2, multiplicação))
    elif op == 3:
        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)
    elif op == 4:
        print("==== Informe os novos valores ====")
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
    elif op == 5:
        print("Saindo do Programa...")
    else:
        print("Opção Inválida!!!")
    print("=-="*10)
print("FIM DO PROGRAMA VOLTE SEMPRE!!!")