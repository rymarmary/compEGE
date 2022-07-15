def f(n):
    d = 1
    k = 0
    dmax = 1
    while d * d <= n:
        if n % d == 0:
            if n // d - d <= 90:
                k += 1
            if k == 3:
                break
        d += 1
        dmax = max(d, dmax)
    return k

for i in range(5 * 10 ** 5, 10 ** 6 + 1):
    if f(i) >= 3:
        print(i, dmax)
