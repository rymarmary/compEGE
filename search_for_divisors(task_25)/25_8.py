def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

k = 0
maxi = 0
for i in range(125697, 190235):
    d = 2
    while d * d < i:
        if i % d == 0:
            if isprime(d):
                if isprime(i // d):
                    k += 1
                    if i > maxi:
                        maxi = i
                    break
        d += 1
print(k, maxi)
