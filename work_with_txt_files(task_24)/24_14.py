f = open('k8-69.txt')
s = f.readline()
symb = 0
symbm = 1
symbmax1 = 1
symbmax2 = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        symbm += 1
        if symbm > symbmax1:
            symbmax1 = symbm
            symb = s[i]
    else:
        symbm = 1
symbm = 1
for j in range(len(s) - 1):
    if s[i] == s[i + 1]:
        symbm += 1
        if symbm > symbmax2:
            symbmax2 = symbm
    else:
        symbm = 1
        if symbmax1 == symbmax2:
            print(s[j])
            break
print(symb, symbmax1)
        
