f = open('24.txt').read()
a = ''
max_count = 1
for i in range(len(f)):
    if ('XY' not in a) and ('XZ' not in a):
        a = a + f[i]
        max_count = max(len(a), max_count)
    else:
        a = a[-1]
print(max_count)
