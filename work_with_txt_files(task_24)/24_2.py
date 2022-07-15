f = open('k7a-1.txt', 'r').read()
kmax = 1
kt = 1
for i in range(len(f) - 1):
    if (f[i] == 'A' or f[i] == 'B' or f[i] == 'C') and (f[i + 1] == 'A' or f[i + 1] == 'B' or f[i + 1] == 'C'):
        kt += 1
        if kt > kmax:
            kmax = kt
    else:
        kt = 1
print(kmax)
