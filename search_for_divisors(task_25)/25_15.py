for i in range(153222, 153271):
    d = 1
    k = 0
    while d * d <= i // 2:
        if (i - d * d ) ** 0.5 == int((i - d * d) ** 0.5):
            k += 1
            x = d
            if k > 1:
                break
        d += 1
    if k == 1:
        print(i, x, (i - x * x ) ** 0.5)
        
