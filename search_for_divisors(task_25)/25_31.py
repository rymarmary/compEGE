def kdel(n):
    d = 2
    count = 0
    while d * d < n:
        if n % d == 0:
            count += 2
        d += 1
    if d * d == n:
        count += 1
    return count

for i in range(26600, 28101):
    if kdel(i) > 0 and kdel(i) % 13 == 0:
        print(i, kdel(i))
