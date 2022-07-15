s = open('k7-m1.txt')
f = s.readline()
kt = 1
kmin = 10 ** 6
chains = 0
for i in range(len(f) - 1):
    if f[i] == 'C' and f[i + 1] == 'C':
        kt += 1
        if kt == 2:
            chains += 1
        
    else:
        kt = 1
        if kt > 1 and kt < kmin:
            kmin = kt
if kt < kmin:
    kmin = kt
if kmin == 10 ** 6:
    print(0)
else:
    print(kmin)
print(chains, len(f))
s.close()
