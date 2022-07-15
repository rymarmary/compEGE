def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

count = 0
minim = 10 ** 7
for i in range(173225, 217438):
    d = 2
    while d * d < i:
        if i % d == 0:
            if isprime(d) and isprime(i // d):
                if d % 10 == (i // d) % 10:
                    count += 1
                    minim = min(i, minim)
        d += 1
print(count, minim)
    
