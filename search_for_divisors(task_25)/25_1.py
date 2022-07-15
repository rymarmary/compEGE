del_1 = 0
del_2 = 0
for n in range(174457, 174506):
    d = 2
    k = 2
    while d * d < n:
        if n % d == 0:
            k += 2
            del_1 = d
            del_2 = n // d
            if k > 4:
                break
        d += 1
    if d * d == n:
        k += 1
    if k == 4:
        print(n, del_1, del_2)
