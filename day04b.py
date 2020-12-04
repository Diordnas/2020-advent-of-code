f=open('d').read().split('\n\n')
s=['byr','iyr','eyr','hgt','hcl','ecl','pid']
h='1234567890abcdef'
c=['amb','blu','brn','gry','grn','hzl','oth']
a=0
for p in f:
 validkeys=0
 for k in p.split():
  k=k.split(':')
  if k[0]==s[0]:validkeys+=1920<=int(k[1])<=2002
  if k[0]==s[1]:validkeys+=2010<=int(k[1])<=2020
  if k[0]==s[2]:validkeys+=len(k[1])==4 and 2020<=int(k[1])<=2030
  if k[0]==s[3]and k[1][-2:]=='cm':validkeys+=150<=int(k[1][:-2])<=193
  if k[0]==s[3]and k[1][-2:]=='in':validkeys+=59<=int(k[1][:-2])<=76
  if k[0]==s[4]:validkeys+=k[1][0]=='#'and sum(i in h for i in k[1][1:])==6
  if k[0]==s[5]:validkeys+=k[1]in c
  if k[0]==s[6]:validkeys+=len(k[1])==9
 if validkeys==7:a+=1
print(a)
