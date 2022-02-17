p = float(input())
c = float(input())
e = input()
p_f = 0
if p <= 50:
	if e == "CTT":
		p_f = p + 3.95 - c
	elif e == "LOJA":
		p_f = p - c
elif p > 50:
	if e == "CTT":
		p_f = p - c
	elif e == "LOJA":
		p_f = p-c
print("%.2f"%p_f)