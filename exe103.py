def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} Gol(s) no campeonato')

n = str(input("Nome do Jogador: "))
g = str(input("Números de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n. strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)