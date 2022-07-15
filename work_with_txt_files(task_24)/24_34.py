f = open('24-s1.txt')
ks = 1
kx = 1
k = 0
for s in f:
    ks = 1
    kx = 1
    for i in range(len(s)):
        if s[i] == 'S':
            ks += 1
        elif s[i] == 'X':
            kx += 1
    if ks == kx:
        k += 1
print(k)
f.close()
