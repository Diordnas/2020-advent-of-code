f=open('d').read().split('\n\n')
s=['byr','iyr','eyr','hgt','hcl','ecl','pid']
print(sum([sum([k in p for k in s])==7 for p in f]))
