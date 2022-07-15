s = open('k7c-5.txt')
f = s.readline()
k = 0
for i in range(len(f) - 4):
    if f[i] != f[i + 1] and f[i + 1] != f[i + 2] and f[i + 2] != f[i + 3] and f[i + 3] != f[i + 4]:
        k += 1
print(k)
        
