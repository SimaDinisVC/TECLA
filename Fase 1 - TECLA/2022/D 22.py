palavra = input()
palavr = []
for i in palavra:
    palavr.append(i)
linhas, colunas = input().split()
linhas = int(linhas)
linha = []
colunas = int(colunas)
for o in range(linhas):
    linha.append(input().split())
    print(linha)
for i in range(len(linhas)):
    if linha[i] == palavra:
        linha[i][i+1]
#####This is a tentative solution as we have no knowledge of matrices at the moment#####