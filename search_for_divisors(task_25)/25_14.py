'''def f(n):
    d = 2
    sumd = 1
    dell = []
    while d * d < n:
        if n % d == 0:
            dell.append(d)
            dell.append(n // d)
            sumd += d + n // d
        d += 1
    if d * d == n:
        dell.append(d)
        sumd += d
    if sumd >= n:
        print(n, sumd - n, dell)

for i in range(300, 351):
    f(i)'''

for i in range(300, 351):
    d = 2
    m = []
    sumdel = 1
    while d * d < i:
        if i % d == 0:
            m.append(d)
            m.append(i // d)
            sumdel += d + i // d
        d += 1
    if i < sumdel:
        m.sort()
        print(i, end = ' ')
