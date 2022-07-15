f = open('24-1.txt')
s = f.readline()
maxindex = 0
maxlen = 0
k = 1
index = 0

for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        k += 1
        if index == 0:
            index = i
    else:
        if k > maxlen:
            maxlen = k
            maxindex = index
        index = 0
        k = 1
        
print(maxindex + 1)
f.close()
