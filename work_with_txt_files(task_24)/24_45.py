f = open('24-B.txt')
s = f.readline()
'''st = ''
res = 0
for i in range(len(s)):
    if (s[i] != '+') and (s[i] != '-'):
        st += s[i]
    else:
        if s[i] == '+':
            res = res + int(st)
            st = str()
        if s[i] == '-':
            res = res - int(st)
            st = str()'''
print(eval(s))
f.close()
