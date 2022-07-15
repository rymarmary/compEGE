def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def prime2(n, k):
    d = 2
    while d * d < n:
        if n % d == 0 and d != k and (n // d) != k:
            if isprime(d):
                if isprime(n // d):
                    return True
        d += 1
    return False
            

k, maxi = 0, 0
for i in range(105673, 220785):
    d = 2
    while d * d < i:
        if i % d == 0:
            if isprime(d):
                if prime2(i // d, d):
                    k += 1
                    if i > maxi:
                        maxi = i
            break
        d += 1
        
print(k, maxi)
    
