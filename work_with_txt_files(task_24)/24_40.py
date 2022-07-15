f = open('24-j3.txt')
s = f.readline()
print(s.count('TIK') + s.count('TOK'))
f.close()
