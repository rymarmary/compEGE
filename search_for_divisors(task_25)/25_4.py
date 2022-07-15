for i in range(81234, 134690):
    k = 0
    s = ''
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k += 1
            s = s + str(j) + ' '
        if k > 3:
            break
    if k == 3:
        print(s)
