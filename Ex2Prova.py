s =0
cont = 0
n = []
for i in range (0,10):
    n.append(int(input()))
    s = s + n[i]

m = s/10

for i in range(0,10):
    if (n[i] < m):
        cont = cont+1

print(cont)