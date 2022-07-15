f = open('1.txt')
k = 0
kmax = 0
s = f.readline()
for i in range(len(s)):
    if s[i] != 'Z':
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 0
print(kmax)
f.close()
