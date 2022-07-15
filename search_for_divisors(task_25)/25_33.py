def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def sumdel(n):
    sumd = 0
    d = 2
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                sumd += d
            if isprime(n // d):
                sumd += n // d
        d += 1
    return sumd

count = 0
for i in range(650000, 660000):
    n = sumdel(i)
    if n % 10 == 5:
        count += 1
        print(i, n)
        if count == 5:
            break
