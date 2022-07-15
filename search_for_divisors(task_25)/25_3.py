def koldel(n):
    a = []
    d = 1
    k = 0
    while d * d < n:
        if n % d == 0:
            k += 2
            a.append(d)
            a.append(n // d)
            if k > 6:
                break
        d += 1
    if d * d == n:
        k += 1
        a.append(d)
    if k == 6:
        print(a)

for i in range(193136, 193224):
    koldel(i)
