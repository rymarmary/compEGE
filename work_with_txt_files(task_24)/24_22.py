f = open('24-s1.txt')
k = 0
for s in f:
    for i in range(len(s) - 2):
        if s[i] == 'A' and s[i + 2] == 'R':
            k += 1
            break
print(k)
f.close()
