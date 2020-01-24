num = int(input("Digite um numero inteiro: "))
print('''>>> Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print("{} em Binário é igual à {}.".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} em Octal é igual à {}.".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} em Hexadecimal é igual à {}.".format(num, hex(num)[2:]))
else:
    print("Opção inválida, digite um valor válido!")