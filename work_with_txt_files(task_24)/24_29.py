f = open('24-j6.txt')
s = f.readline()
k = 1
kpod = 0
for i in range(len(s) - 1):
    if s[i + 1] > s[i]:
        k += 1
    else:
        if k == 5:
            kpod += 1
        k = 1
if k == 5:
    kpod += 1
print(kpod)
f.close()
