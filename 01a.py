a=[int(i)for i in open('a').readlines()];print([n*m for n in a for m in a if n+m==2020][0])
