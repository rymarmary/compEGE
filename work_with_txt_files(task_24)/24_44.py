f = open('24-5.txt')
s = f.readline()
f.close()
k, maxk = 0, 0
for i in range(len(s) - 1):
    if s[i] == '(' and s[i + 1] == ')':
        k += 1
        maxk = max(k, maxk)
    elif s[i] ==s[i + 1]:
        k = 0
print(maxk)
