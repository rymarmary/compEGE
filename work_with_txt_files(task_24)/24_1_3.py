f = open('24-5.txt')
s = f.readline()
kotk = 0
k = 0
for i in range(len(s)):
    if s[i] == '(':
        kotk += 1
    elif s[i] == ')' and kotk != 0:
        kotk -= 1
        k += 1
print(k)
f.close()
