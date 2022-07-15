def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

for i in range(2532000, 2532161):
    if isprime(i) == True:
        if i % 10 == 7:
            print(i)
