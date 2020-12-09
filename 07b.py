f=open('g').read().split('.\n')[:-1]
rules=[[rule.split(' contain ')[0].replace('bags','bag').replace(' bag','')]+[i for i in rule.split(' contain ')[1].replace('bags','bag').replace(' bag','').split(', ')]for rule in f]
def get(item):return [i[1:] for i in rules if i[0]==item][0]
def countBags(item):
    contains= get(item)
    if contains==["no other"]:return 0
    return sum([int(i[0])*(countBags(i[2:])+1) for i in contains])
print(countBags("shiny gold"))
