def koldel(n):
    a = []
    d = 1
    k = 0
    while d * d < n:
        if n % d == 0:
            k += 2
            a.append(d)
            a.append(n // d)
            if k > 5:
                break
        d += 1
    if d * d == n:
        k += 1
        a.append(d)
    if k == 5:
        print(a)

for i in range(11275, 16329):
    if i ** 0.5 == int(i ** 0.5):
        koldel(i)
