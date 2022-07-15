def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

for i in range(194441, 196501):
    if isprime(i) == True:
        if i % 100 == 93:
            print(i)
