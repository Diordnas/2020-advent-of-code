f=[0]+sorted([int(i) for i in open('j').read().splitlines()])
l=[f[i+1]-f[i] for i in range(len(f)-1)]
print(l.count(1)*(l.count(3)+1))
