f = open('24-j9.txt')
s = f.readline()
k = 0
for i in range(len(s) // 2):
    if s[i] == s[len(s) - i - 1]:
        k += 1
print(k)
f.close()
