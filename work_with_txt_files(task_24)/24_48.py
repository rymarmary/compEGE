f = open('k8-0.txt')
s = f.readline()
k = 1
kmax = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
kmax = max(kmax, k)
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
        if k == kmax:
            print(s[i], kmax, end = ' ')
    else:
        k = 1
