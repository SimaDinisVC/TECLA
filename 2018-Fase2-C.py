jurados = int(input())
notas = input()
votoA = 0
votoB = 0
for i in range(0,jurados):
    voto = notas[i:i+1]
    if voto == "A":
        votoA = votoA + 1
    else:
        votoB = votoB + 1
if votoA > votoB:
    print("A")
elif votoA < votoB:
    print("B")
else:
    print("Empate")