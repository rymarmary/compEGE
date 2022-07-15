f = open('24-153.txt')
s = f.readline()
k = 0
for i in range(len(s) - 10):
    if s[i] == 'A':
        for z in range(i + 6, i + 10):
            if s[z] == 'F':
                k += 1
print(k)
f.close()
