f=open('h').read().splitlines()
def run(file):
    e=[]
    l=0
    a=0
    while True:
     if l>=len(file):return a
     i=file[l]
     e+=[l]
     if i[0:3]=="acc":
      a+=int(i[3:])
      l+=1
     if i[0:3]=="jmp":l+=int(i[3:])
     if i[0:3]=="nop":l+=1
     if l in e:return 'bad'
for line in range(len(f)):
    if f[line][0]!='a':
        copy=f[:]
        if f[line][0]=='n':
            copy[line]='jmp'+copy[line][3:]
        if f[line][0]=='j':
            copy[line]='nop'+copy[line][3:]
        result=run(copy)
        if result != 'bad':print(result)
