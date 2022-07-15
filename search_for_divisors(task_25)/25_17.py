def sumdel(n):
    d = 2
    sumd = 0
    while d * d < n:
        if n % d == 0:
            sumd += d + n // d
        d += 1
    if d * d == n:
        sumd += d
    return sumd

def countdel(n):
    d = 2
    kdel = 0
    while d * d < n:
        if n % d == 0:
            kdel += 2
        d += 1
    if d * d == n:
        kdel += 1
    return kdel

for i in range(135790, 163229):
    if sumdel(i) > 460000:
        print(countdel(i), sumdel(i), end = ' ')

    
    
    
