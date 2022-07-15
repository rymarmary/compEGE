f = open('24-5.txt')
s = f.readline()
a = []
for i in range(len(s)):
    if s[i] == ')':
        a.append(i + 1)
print(a[9999])  
f.close()
