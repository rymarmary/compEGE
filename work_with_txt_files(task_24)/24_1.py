f = open('k7-100.txt', 'r').read()
kmax = 1 #заведомо ложное число
kt = 1
for i in range(len(f)-1):
    if f[i] == 'C' and f[i + 1] == 'C':
        kt += 1
        if kmax < kt:
            kmax = kt
    else:
        kt = 1
print(kmax)
