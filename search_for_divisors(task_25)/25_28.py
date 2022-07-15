def chet(n):
    if (n % 10) % 2 == 0 and (n // 100) % 2 == 0:
        if (n // 10000) % 2 != 0 and (n // 1000) % 2 != 0 and (n // 10) % 2 != 0:
            return True

count = 0
min_ch = 10 ** 7
max_ch = 0
for i in range(33333, 55556):
    if chet(i) == True:
        if i % 6 != 0 and i % 7 != 0 and i % 8 != 0:
            count += 1
            min_ch = min(i, min_ch)
            max_ch = max(i, max_ch)
print(count, max_ch - min_ch)
