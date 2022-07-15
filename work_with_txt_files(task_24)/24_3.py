f = open('k8-1.txt', 'r').read()
kmax = 1
kt = 1
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        kt += 1
        if kt > kmax:
            kmax = kt
    else:
        kt = 1
print(kmax)
