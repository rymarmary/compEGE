f = open('24-1.txt')
s = f.readline()
f.close()
a = ''
a_min = 10 ** 6
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        a = a + s[i]
    else:
        if a != '':
            if int(a) % 2 != 0:
                if int(a) < a_min:
                    a_min = int(a)
        a = ''
print(a_min)
