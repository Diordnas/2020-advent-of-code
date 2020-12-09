s=[int(i.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)for i in open('e').read().splitlines()]
print([i for i in range(1024)if i not in s and i-1 in s and i+1 in s][0])
