def sumdel(n):
    d = 2
    sumd = 1
    while d * d < n:
        if n % d == 0:
            sumd += d + n // d
        d += 1
    if d * d == n:
        sumd += d
    return sumd

for i in range(1000, 20001):
    if i - sumdel(i) == 1:
        print(i)
        
