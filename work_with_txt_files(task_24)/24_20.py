f = open('k7c-1.txt')
s = f.readline()
k = 0
for i in range(len(s) - 2):
    if s[i] in 'BCD':
        if (s[i + 1] in 'BDE') and (s[i + 1] != s[i]):
            if (s[i + 2] in 'BCE') and (s[i + 2] != s[i + 1]):
                k += 1
print(k)
f.close()
