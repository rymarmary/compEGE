f = open('27.txt')
n = int(f.readline()) # считали кол-во из первой строки
s = 0
mind = 1000000
for i in range(n):
    x = f.readline()
    x = x.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    s += max(x)
    x.sort(reverse = True)
    if (x[0] - x[1]) % 101 != 0 and (x[0] - x[1]) < mind:
        mind = x[0] - x[1]
    if (x[0] - x[2]) % 101 != 0 and (x[0] - x[2]) < mind:
        mind = x[0] - x[2]
if s % 101 != 0:
    print(s)
else:
    print(s - mind)
    
            
