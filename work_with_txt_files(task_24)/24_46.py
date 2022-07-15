f = open('24-j9.txt')
s = f.readline()
k = 0
for i in range(1, len(s) - 2):
    if s[i - 2] == s[i + 2] and s[i - 1] == s[i + 1]:
        k += 1
print(k)
f.close()
