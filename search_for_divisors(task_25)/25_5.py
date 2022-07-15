def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

for i in range(2943444, 2943530):
    if isprime(i) == True:
        print(i)
