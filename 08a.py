f=open('h').read().splitlines()
e = []
l = 0
a=0
while True:
 i=f[l]
 e+=[l]
 if i[0:3]=="acc":
  a+=int(i[3:])
  l+=1
 if i[0:3]=="jmp":l+=int(i[3:])
 if i[0:3]=="nop":l+=1
 if l in e: break
print(a)
