c, l = input().split() 
d = int(input())
c = int(c) 
l = int(l)
c = c * 100
l = l * 100
total = int((c//d) * (l//d))
print(total)