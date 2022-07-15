f = open('k7a-5.txt', 'r').read()
kt = 1
kmax = 1
for i in range(len(f) - 1):
    if f[i] != 'C' and f[i] != 'F' and f[i + 1] != 'C' and f[i + 1] != 'F':
        kt += 1
        if kt > kmax:
            kmax = kt
    else:
        kt = 1
print(kmax)
