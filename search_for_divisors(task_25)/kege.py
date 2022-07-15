def sumdel(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return d + n // d
        d += 1
    return 1
k = 0
for i in range(250200, 1000000):
    if sumdel(i) % 123 == 17:
        k += 1
        print(i, sumdel(i))
        if k == 5:
            break
    
