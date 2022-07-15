def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def prime2(n, k):
    d = 2
    while d * d < n and d != k and n // d != k:
        if d % 10 == k % 10 and (n // d) % 10 == k % 10:
            if n % d == 0:
                if prime(d):
                    if prime(n // d):
                        return True
        d += 1
    return False

k, maxi = 0, 0
mini = 10 ** 7
for i in range(416782, 498325):
    d = 2
    while d * d < i:
        if i % d == 0:
            if prime(d):
                if prime2(i // d, d):
                    k += 1
                    mini = min(i, mini)
                    maxi = max(i, maxi)
                    break
        d += 1
print(k, maxi - mini)
