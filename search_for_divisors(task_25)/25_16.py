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

k = 0
for i in range(2, 20001):
    if sumdel(i) > i:
        k += 1
print(k)
    
    
    
