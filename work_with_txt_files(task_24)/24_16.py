f = open('k7b-1.txt')
s = f.readline()
k = 1
maxk = 1
for i in range(len(s)):
    if (k % 3 == 0 and s[i] == 'E') or (k % 3 == 1 and s[i] == 'A') or (k % 3 == 2 and s[i] == 'B'):
        k += 1
        if k > maxk:
            maxk = k
    else:
        k = 1
print(maxk)
f.close()
