f = open('27-b.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in pair]
    s1 = [0] * 3
    for x in cmb:
        s1[x % 3] = max(s1[x % 3], x)
    s = [x for x in s1 if x != 0]
    
m = max(x for x in s if x % 3 != 0)
print(m)
