f=open('g').read().split('.\n')[:-1]
rules=[[rule.split(' contain ')[0].replace('bags','bag').replace(' bag','')]+[i[2:] for i in rule.split(' contain ')[1].replace('bags','bag').replace(' bag','').split(', ')]for rule in f]
queue = [i[0] for i in rules if "shiny gold" in i[1:]]
checked = ["shiny gold"]
while len(queue):
 item = queue[0]
 queue = queue[1:]
 checked+=[item]
 neighbours = [i[0] for i in rules if item in i[1:]]
 for i in neighbours:
  if i not in checked and i not in queue:
   queue+=[i]
print(len(checked)-1)
