# PRIMEIRA OPÇÃO
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print("\n***FIM***")
# SEGUNDA OPÇÃO
for n in range(2, 51, 2):
    print("...", end='')
    if n % 2 == 0:
        print(n, end=' ')
print("\n***FIM***")
