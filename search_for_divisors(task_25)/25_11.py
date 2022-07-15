def f(n):
    d = int(n ** 0.5) - 65
    k = 0
    while d * d <= n:
        if n % d == 0:
            if n // d - d <= 100:
                k += 1
            if k == 3:
                break
        d += 1
    return k

for i in range(10 ** 6, 2 * 10 ** 6 + 1):
    if f(i) >= 3:
        print(i)
