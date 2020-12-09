print(max([int(i.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)for i in open('e').read().splitlines()]))
