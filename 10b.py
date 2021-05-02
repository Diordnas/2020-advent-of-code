f=[0]+sorted([int(i) for i in open('j').read().splitlines()])
def check(copy): return len(set([copy[i+1]-copy[i] for i in range(len(copy)-1)]+[1,2,3]))==3
print(2**(len(f)-2))
for i in range(2**(len(f)-2)):
    code=str(bin(i))[2:]
    code = ('0'*(len(f)-2-len(code)))+code
print("yeet")
