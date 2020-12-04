import math
f=open('c').readlines()
s=[[1,1],[3,1],[5,1],[7,1],[1,2]]
print(math.prod([sum([f[i][(i*c[0]//c[1])%(len(f[0])-1)]=='#'for i in range(c[1],len(f),c[1])])for c in s]))
