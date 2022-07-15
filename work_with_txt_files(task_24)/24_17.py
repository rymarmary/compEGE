s = open('k7b-5.txt')
f = s.readline()
k = 1
kmax = 1
for i in range(len(f)):
    if (k % 2 == 0 and f[i] == 'C') or (k % 2 == 1 and f[i] == 'A'):
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
print(kmax)
