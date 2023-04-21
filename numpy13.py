import numpy as np
a=[]
b=int(input("SIZE"))
c=int(input("SIZE"))
for i in range(b):
    d=[]
    for j in range(c):
        e=int(input("Enter"))
        d.append(e)
    a.append(d)
v=np.array(a)
for i in range(b):
    for j in range(c):
        print(v[i][j],end="")
    print()
print()
v=v[:2,1:]
print(v)