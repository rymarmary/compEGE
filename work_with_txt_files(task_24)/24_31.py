f = open('24-j8.txt')
s = f.readline()
k = 1
kmax = 1
for i in range(len(s) - 1):
    if s[i] != '\n' and s[i + 1] != '\n':
        if int(s[i]) + int(s[i + 1]) >= 10:
            k += 1
            if k > kmax:
                kmax = k
        else:
            k = 1
print(kmax)
f.close()
