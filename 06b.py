f=open('f').read().split('\n\n')
f[len(f)-1]=f[len(f)-1][:-1]
s=0
for i in f:
    for j in range(ord('a'),ord('z')+1):
        s+= i.count(chr(j))==i.count('\n')+1
print(s)
