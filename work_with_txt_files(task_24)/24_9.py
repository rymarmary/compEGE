s = open('24-j5.txt')
f = s.readline()
k = f.count('OCK') - f.count('STOCK')
print(k)
s.close()
    
