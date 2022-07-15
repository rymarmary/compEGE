f = open('24.txt')
s = f.readline()
count = 0
count_max = 0
for i in range(len(s)):
    if s[i] != 'C' and s[i] != 'F':
        count += 1
        count_max = max(count, count_max)
    else:
        count = 0
        
print(count_max)
        
