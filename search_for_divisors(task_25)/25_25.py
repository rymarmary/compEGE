def koldel(n):  #числа, имеющие макс кол-во делителей. если несколько, то мин из них
    d = 2       #вывести кол-во делителей числа и два максимальных
    k = 2
    while d *d < n:
        if n % d == 0:
            k += 2
        d += 1
    if d * d == n:
        k += 1
    return k

def max2(n):
    print(n)
    d = 2
    while d * d < n:
        if n % d == 0:
            print(n // d)
            break
        d += 1
            
    
ch = 0
tkol = 0
maxkol = 0
for i in range(394441, 394506):
    tkol = koldel(i)
    if tkol > maxkol:
        maxkol = tkol
        ch = i
print(maxkol)
max2(ch)
    
        
