f=open('c').readlines()
print(sum([f[i][(i*3)%(len(f[0])-1)]=='#'for i in range(1,len(f))]))
