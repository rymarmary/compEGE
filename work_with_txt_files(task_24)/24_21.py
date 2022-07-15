f = open('24.txt')
s = f.readline()
k = 1
kmax = 1
for i in range(len(s) - 1):
    if ord(s[i]) < ord(s[i + 1]):
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
print(kmax)
f.close()
    
