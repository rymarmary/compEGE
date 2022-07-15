f = open('1.txt')
k = 1
kmax = 1
s = f.readline()
ch = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        k += 1
        if k > kmax:
            kmax = k
            ch = s[i]
    else:
        k = 1
print(ch, kmax)
f.close()
