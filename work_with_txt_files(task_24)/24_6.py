s = open('k7a-6.txt')
f = s.readline()
kt = 1
kmax = 1
for i in range(len(f) - 1):
    if f[i] != 'A' and f[i] != 'E' and f[i + 1] != 'A' and f[i + 1] != 'E':
        kt += 1
        if kt > kmax:
            kmax = kt
    else:
        kt = 1
print(kmax)
