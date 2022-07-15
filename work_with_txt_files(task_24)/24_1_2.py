f = open('24-s1.txt')
k = 0
flag = 0
for s in f:
    flag = 0
    for i in range(len(s) - 2):
        if s[i] == 'F' and s[i + 2] == 'O':
            flag = 1
            break
    if flag == 1:
        k += 1
print(k)
