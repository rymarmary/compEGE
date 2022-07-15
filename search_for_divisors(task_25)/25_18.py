def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def summ(n):
    n = str(n)
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    return summ

for i in range(33333, 55556):
    if isprime(i):
        if summ(i) > 35:
            print(i, summ(i), end = ' ')
