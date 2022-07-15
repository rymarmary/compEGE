def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

mind = 10 ** 7
d1, d2 = 0, 0
for i in range(523456, 578926):
    d = 2
    while d * d < i:
        if i % d == 0:
            if isprime(d) and isprime(i // d):
                if i // d - d < mind:
                    mind = i // d - d
                    d1 = d
                    d2 = i // d
        d += 1
print(d1, d2)
