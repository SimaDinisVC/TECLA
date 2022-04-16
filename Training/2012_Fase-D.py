emp1= input().split()
emp2=input().split()
emp3=input().split()
emp4=input().split()
escolha=input().split()
for i in range(0,len(escolha)):
    escolha[i]=int(escolha[i])
if escolha.count(1) >= 1:
    linha1 = "|* "
else:
    linha1 = "|  "
if escolha.count(2) >= 1:
    linha1 = linha1 + "* "
else:
    linha1 = linha1 + "  "
if escolha.count(3) >= 1:
    linha1 = linha1 + "* "
else:
    linha1 = linha1 + "  "
if escolha.count(4) >= 1:
    linha1 = linha1 + "* "
else:
    linha1 = linha1 + "  "
if escolha.count(1) >= 2:
    linha2 = "|* "
else:
    linha2 = "|  "
if escolha.count(2) >= 2:
    linha2 = linha2 + "* "
else:
    linha2 = linha2 + "  "
if escolha.count(3) >= 2:
    linha2 = linha2 + "* "
else:
    linha2 = linha2 + "  "
if escolha.count(4) >= 2:
    linha2 = linha2 + "* "
else:
    linha2 = linha2 + "  "
if escolha.count(1) >= 3:
    linha3 = "|* "
else:
    linha3 = "|  "
if escolha.count(2) >= 3:
    linha3 = linha3 + "* "
else:
    linha3 = linha3 + "  "
if escolha.count(3) >= 3:
    linha3 = linha3 + "* "
else:
    linha3 = linha3 + "  "
if escolha.count(4) >= 3:
    linha3 = linha3 + "* "
else:
    linha3 = linha3 + "  "
if escolha.count(1) >= 4:
    linha4 = "|* "
else:
    linha4 = "|  "
if escolha.count(2) >= 4:
    linha4 = linha4 + "* "
else:
    linha4 = linha4 + "  "
if escolha.count(3) >= 4:
    linha4 = linha4 + "* "
else:
    linha4 = linha4 + "  "
if escolha.count(4) >= 4:
    linha4 = linha4 + "* "
else:
    linha4 = linha4 + "  "
if escolha.count(1) >= 5:
    linha5 = "|* "
else:
    linha5 = "|  "
if escolha.count(2) >= 5:
    linha5 = linha5 + "* "
else:
    linha5 = linha5 + "  "
if escolha.count(3) >= 5:
    linha5 = linha5 + "* "
else:
    linha5 = linha5 + "  "
if escolha.count(4) >= 5:
    linha5 = linha5 + "* "
else:
    linha5 = linha5 + "  "
if escolha.count(1) >= 6:
    linha6 = "|* "
else:
    linha6 = "|  "
if escolha.count(2) >= 6:
    linha6 = linha6 + "* "
else:
    linha6 = linha6 + "  "
if escolha.count(3) >= 6:
    linha6 = linha6 + "* "
else:
    linha6 = linha6 + "  "
if escolha.count(4) >= 6:
    linha6 = linha6 + "* "
else:
    linha6 = linha6 + "  "
if escolha.count(1) >= 7:
    linha7 = "|* "
else:
    linha7 = "|  "
if escolha.count(2) >= 7:
    linha7 = linha7 + "* "
else:
    linha7 = linha7 + "  "
if escolha.count(3) >= 7:
    linha7 = linha7 + "* "
else:
    linha7 = linha7 + "  "
if escolha.count(4) >= 7:
    linha7 = linha7 + "* "
else:
    linha7 = linha7 + "  "
if escolha.count(1) >= 8:
    linha8 = "|* "
else:
    linha8 = "|  "
if escolha.count(2) >= 8:
    linha8 = linha8 + "* "
else:
    linha8 = linha8 + "  "
if escolha.count(3) >= 8:
    linha8 = linha8 + "* "
else:
    linha8 = linha8 + "  "
if escolha.count(4) >= 8:
    linha8 = linha8 + "* "
else:
    linha8 = linha8 + "  "
if escolha.count(1) >= 9:
    linha9 = "|* "
else:
    linha9 = "|  "
if escolha.count(2) >= 9:
    linha9 = linha9 + "* "
else:
    linha9 = linha9 + "  "
if escolha.count(3) >= 9:
    linha9 = linha9 + "* "
else:
    linha9 = linha9 + "  "
if escolha.count(4) >= 9:
    linha9 = linha9 + "* "
else:
    linha9 = linha9 + "  "
if escolha.count(1) >= 10:
    linha10 = "|* "
else:
    linha10 = "|  "
if escolha.count(2) >= 10:
    linha10 = linha10 + "* "
else:
    linha10 = linha10 + "  "
if escolha.count(3) >= 10:
    linha10 = linha10 + "* "
else:
    linha10 = linha10 + "  "
if escolha.count(4) >= 10:
    linha10 = linha10 + "* "
else:
    linha10 = linha10 + "  "
if escolha.count(1) >= 11:
    linha11 = "|* "
else:
    linha11 = "|  "
if escolha.count(2) >= 11:
    linha11 = linha11 + "* "
else:
    linha11 = linha11 + "  "
if escolha.count(3) >= 11:
    linha11 = linha11 + "* "
else:
    linha11 = linha11 + "  "
if escolha.count(4) >= 11:
    linha11 = linha11 + "* "
else:
    linha11 = linha11 + "  "
if escolha.count(1) >= 12:
    linha12 = "|* "
else:
    linha12 = "|  "
if escolha.count(2) >= 12:
    linha12 = linha12 + "* "
else:
    linha12 = linha12 + "  "
if escolha.count(3) >= 12:
    linha12 = linha12 + "* "
else:
    linha12 = linha12 + "  "
if escolha.count(4) >= 12:
    linha12 = linha12 + "* "
else:
    linha12 = linha12 + "  "
print("^         ")
if linha12 != "|        ":
    print(linha12)
if linha11 != "|        ":
    print(linha11)
if linha10 != "|        ":
    print(linha10)
if linha9 != "|        ":
    print(linha9)
if linha8 != "|        ":
    print(linha8)
if linha7 != "|        ":
    print(linha7)
if linha6 != "|        ":
    print(linha6)
if linha5 != "|        ":
    print(linha5)
if linha4 != "|        ":
    print(linha4)
if linha3 != "|        ":
    print(linha3)
if linha2 != "|        ":
    print(linha2)
if linha1 != "|        ":
    print(linha1)
print("+-------->")
print(" 1 2 3 4")
print("\nO {} teve direito a {} jantares.".format(emp1[1],escolha.count(1)))
print("O {} teve direito a {} jantares.".format(emp2[1],escolha.count(2)))
print("O {} teve direito a {} jantares.".format(emp3[1],escolha.count(3)))
print("O {} teve direito a {} jantares.".format(emp4[1],escolha.count(4)))