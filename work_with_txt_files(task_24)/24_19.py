f = open('24-s1.txt')
k = 0
for s in f:
    for i in range(len(s) - 2):
        if s[i] == 'F' and s[i + 2] == 'O':
            k += 1
            break
print(k)
f.close()
