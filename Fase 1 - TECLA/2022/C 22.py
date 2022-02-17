n = input()
ns = []
for i in n:
    if  i == "0":
        ns.append("zero")
    if  i == "1":
        ns.append("um")
    if  i == "2":
        ns.append("dois")
    if  i == "3":
        ns.append("tres")
    if  i == "4":
        ns.append("quatro")
    if  i == "5":
        ns.append("cinco")
    if  i == "6":
        ns.append("seis")
    if  i == "7":
        ns.append("sete")
    if  i == "8":
        ns.append("oito")
    if  i == "9":
        ns.append("nove")
print(*ns, sep="-")





