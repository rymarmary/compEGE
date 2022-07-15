f = open('24-s1.txt')
k = 0
for s in f:
    if s.count('K') > s.count('U'):
        k += 1
print(k)
