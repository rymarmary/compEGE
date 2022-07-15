f = open('1.txt')
ka = 0
ke = 0
k = 0
for s in f:
    ke = 0
    ka = 0
    for i in range(len(s)):
        if s[i] == 'A':
            ka += 1
        if s[i] == 'E':
            ke += 1
    if ke > ka:
        k += 1
print(k)
f.close()
