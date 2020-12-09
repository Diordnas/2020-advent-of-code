f=[int(i) for i in open('i').read().splitlines()]
for i in range(len(f)-25):
    if f[i+25] not in [a+b for a in f[i:i+25] for b in f[i:i+25] if a!=b]:print(f[i+25])
