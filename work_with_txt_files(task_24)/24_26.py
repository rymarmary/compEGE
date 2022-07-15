f = open('k7-m25.txt')
s = f.readline()
pos = -1
k = 0
for i in range(len(s) - 2):
    if s[i] < s[i + 1] > s[i + 2]:
        k += 1
        pos = i 
print(k, pos)
