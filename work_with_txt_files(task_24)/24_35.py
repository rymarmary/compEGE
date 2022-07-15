f = open('24-s1.txt')
k = 0
for s in f:
    if s.count('YZ')> 1:
        k += 1
print(k)
f.close()
