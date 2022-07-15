f = open('24-j7.txt')
s = f.readline()
k1 = 1
k1max = 1
k2 = 1
k2max = 1
for i in range(len(s) - 1):
    if s[i] != '\n' and s[i + 1] != '\n':
        if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0:
            k1 += 1
            if k1 > k1max:
                k1max = k1
        elif int(s[i]) % 2 == 1 and int(s[i + 1]) % 2 == 1:
            k2 += 1
            if k2 > k2max:
                k2max = k2
        else:
            k1 = 1
            k2 = 1
print(max(k1max, k2max))
f.close()
    
