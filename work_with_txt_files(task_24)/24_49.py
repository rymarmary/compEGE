f = open('k7c-6.txt')
s = f.readline()
k = 0
for i in range(1, len(s) - 1):
    if s[i - 1] != s[i] and s[i] != s[i + 1] and s[i - 1] != s[i + 1]:
        k += 1
print(k)
f.close()
