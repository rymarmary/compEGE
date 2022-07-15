s = open('24-j5.txt')
f = s.readline()
k = 0
for i in range(len(f) - 2):
    if f[i] == 'K' and f[i + 1] == 'O' and f[i + 2] == 'T':
        k += 1
print(k)
s.close()
    
