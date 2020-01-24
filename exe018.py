import math
angulo = float(input("Digite o numero corresnpondente ao ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O valor do ângulo digitado foi: {}, o seu seno é: {:.2f}, seu cosseno é: {:.2f}, e a sua tangente é:{:.2f}.".format(angulo, seno, cosseno, tangente))
