f = open('24-153.txt')
s = f.readline()
npr = -1
minim = 10 ** 6
for i in range(len(s)):
    if s[i] == 'D' and npr == -1:
        npr = i
    elif s[i] == 'D' and npr != -1:
        if i - npr  + 1 != 2:
            if i - npr + 1 < minim:
                minim = i - npr + 1
        npr = i
print(minim)
f.close()
        
'''f = open('24-153.txt')
a=f.readline()
kmin=99999999
k=0
point=0
for i in range (len(a)):
    if a[i] == 'D':
        point += 1

        if point == 2:
            k=k+1
            point = 1

            if k != 2:
                if k < kmin: kmin = k

            k = 0

    if point == 1:
         k = k+1
print (kmin)         
'''
