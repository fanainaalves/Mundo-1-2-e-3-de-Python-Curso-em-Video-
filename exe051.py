print("="*40)
print(" 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA")
print("="*40)
primeiro_termo = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
for c in range(1, 11, +1):
    pa = primeiro_termo + razão*c
    print(pa, end=" >>> ")
print("FIM DA PROGRESSÃO!!!")