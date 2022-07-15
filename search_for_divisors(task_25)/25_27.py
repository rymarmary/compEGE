def sumn(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

def multn(n):
    mult = 1
    while n > 0:
        mult *= n % 10
        n //= 10
    return mult

for i in range(87921, 88189):
    if sumn(i) % 14 == 0 and multn(i) % 18 == 0 and multn(i) != 0:
        print(sumn(i), multn(i))
