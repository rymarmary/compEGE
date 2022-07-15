f = open('24-1.txt')
s = f.readline()
pos = 0
posm = 0
k = 1
kmax = 0
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        k += 1
        if k > kmax:
            kmax = k
            posm = pos
    else:
        k = 1
        pos = i + 1
print(posm + 1)
f.close()
            
