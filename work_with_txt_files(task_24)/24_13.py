f = open('24-s2.txt')
s = f.readline()
a = [0] * 26
nmax = 0
for i in range(len(s)):
    if s[i] == 'X':
        index = ord(s[i + 1]) - ord('A')
        a[index] += 1
for i in range(len(a)):
    if nmax < a[i]:
        nmax = a[i]
        c = i
print(chr(c + ord('A')), nmax)
f.close()
