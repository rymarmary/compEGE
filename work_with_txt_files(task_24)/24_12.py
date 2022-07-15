s = open('k7c-6.txt')
f = s.readline()
k = 0
for i in range(len(f) - 2):
    if f[i] != f[i + 1] and f[i] != f[i + 2] and f[i + 1] != f[i] and f[i + 1] != f[i + 2] and f[i + 2] != f[i] and f[i + 2] != f[i + 1]:
        k += 1
print(k)
