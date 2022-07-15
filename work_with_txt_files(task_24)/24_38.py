f = open('24-s2.txt')
s = f.readline()
a = [0] * 26
maxi = 0
res = 0
for i in range(1, len(s) - 1):
    if s[i - 1] == 'A' and s[i + 1] == 'C':
        a[ord(s[i]) - ord('A')] += 1
for i in range(len(a)):
    if a[i] > maxi:
        maxi = a[i]
        res = i
print(chr(res + ord('A')), maxi)
        
