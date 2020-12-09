f=open('f').read().split('\n\n')
s=0
for i in f:
    for j in range(ord('a'),ord('z')+1):
        s+= i.count(chr(j))>0
print(s)
