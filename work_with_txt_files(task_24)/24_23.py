f = open('24-1.txt')
s = f.readline()
pos = -1
max1 = 0
for i in range(1, len(s) - 1):
    if s[i-1] < s[i] > s[i + 1] and pos != -1:
        max1 = max(max1, i - pos)
        pos = i
    elif s[i-1] < s[i] > s[i + 1] and pos == -1:
        pos = i
print(max1)
f.close()
        
