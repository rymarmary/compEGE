def sumdel(n):
    sumd = 1
    d = 2
    while d * d < n:
        if n % d == 0:
            sumd += d + n // d
        d += 1
    return sumd

def countdel(n):
    d = 2
    kdel = 1
    while d * d < n:
        if n % d == 0:
            kdel += 2
        d += 1
    return kdel

for i in range(2, 10001):
    if sumdel(i) == i:
        print(i, countdel(i))


        
