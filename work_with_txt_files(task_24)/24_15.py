f = open('24-1.txt')
s = f.readline()
a = ''
amax = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        if int(s[i]) % 2 != 0:
            a = a + s[i]
            if int(a) > amax:
                amax = int(a)
    else:
        a = ''
print(amax)
f.close()
        
