f = open('24-1.txt')
s = f.readline()
k = ''
n = 0
nmax = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        k = k + s[i]
    elif k != '':
        n = int(k)
        if n % 2 != 0 and n > nmax:
            nmax = n
        k = ''
if k != '':
    n = int(k)
    if n % 2 != 0 and n > nmax:
                nmax = n
print(nmax)
f.close()
    
