f = open('27-4a.txt')
n = int(f.readline())
s = [0] * n
count = 0

for i in range(n):
    s[i] = int(f.readline())
for i in range(n - 1):
    for j in range(i + 1, n):
        if (s[i] + s[j]) % 12 == 0:
            count += 1
print(count)
    
