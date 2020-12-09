a=[int(i)for i in open('a').readlines()];print([n*m*o for n in a for m in a for o in a if n+m+o==2020][0])
