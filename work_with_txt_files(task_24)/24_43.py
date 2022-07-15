f = open('24-1.txt')
s = f.readline()
pos = -1
min1 = 0
for i in range(1, len(s) - 1):
    if s[i - 1] > s[i] < s[i + 1] and pos != -1:
        min1 = max(min1, i - pos)
        pos = i
    elif s[i - 1] > s[i] < s[i + 1] and pos == -1:
        pos = i
print(min1)
f.close()
