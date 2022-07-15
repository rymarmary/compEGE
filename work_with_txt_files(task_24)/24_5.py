s = open('k8-0.txt')
f = s.readline()
kt = 1
kmax1 = 1
kmax2 = 1
for i in range(len(f) - 1):
    if f[i] == f[i + 1]:
        kt += 1
        if kt > kmax1:
            kmax1 = kt
    else:
        kt = 1
kt = 1
for j in range(len(f) - 1):
    if f[j] == f[j + 1]:
        kt += 1
        if kt > kmax2:
            kmax2 = kt
    else:
        kt = 1

    if kmax1 == kmax2:
        print(f[j])
        break
print(kmax1)
