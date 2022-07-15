f = open('1.txt')
k = 1
kmax = 1
s = f.readline()
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
print(kmax)
f.close()
