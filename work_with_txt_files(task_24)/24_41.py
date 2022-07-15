f = open('24.txt')
s = f.readline()
a = s[0]
kmax = ''
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        a += s[i + 1]
        if len(a) > len(kmax):
            kmax = a
    else:
        if len(a) > len(kmax):
            kmax = a
        a = s[i + 1]
if len(a) > len(kmax):
            kmax = a
print(kmax)
f.close()
