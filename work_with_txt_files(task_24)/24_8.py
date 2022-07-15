s = open('24-1.txt')
f = s.readline()
k = ''
n = 0
nmin = 10 ** 6
for i in range(len(f)):
    if '0' <= f[i] <= '9':
        k = k + f[i]
    elif k != '':
        n = int(k)
        if n % 2 != 0 and n < nmin:
            nmin = n
        k = ''
if k != '':
    n = int(k)
    if n % 2 != 0 and n < nmin:
        nmin = n
print(nmin)
s.close()
        
