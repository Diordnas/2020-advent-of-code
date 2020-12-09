a=0
n=open('b').readlines()
for i in n:
    q,p=i.split(':')
    r,c=q.split(' ')
    mn,mx=[int(j) for j in r.split('-')]
    a += (p[mn]==c)^(p[mx]==c)
print(a)
