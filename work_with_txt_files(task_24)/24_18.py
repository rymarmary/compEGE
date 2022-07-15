f = open('k7b-2.txt')
s = f.readline()
k = 1
kmax = 1
for i in range(len(s)):
    if (k % 4 == 0 and s[i] == 'D') or (k % 4 == 1 and s[i] == 'B') or (k % 4 == 2 and s[i] == 'A') or (k % 4 == 3 and s[i] == 'C'):
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
print(kmax)
f.close()
