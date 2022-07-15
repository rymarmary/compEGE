f = open('k7-m26.txt')
s = f.readline()
k = 0
pos = -1
for i in range(1, len(s) - 1):
    if s[i - 1] > s[i] < s[i + 1]:
        k += 1
        pos = i - 1
print(k, pos)
f.close()
