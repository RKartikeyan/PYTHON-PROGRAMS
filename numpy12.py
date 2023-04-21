import numpy as np
a=[]
b=int(input("Enter the size of row"))
c=int(input("Enter the size of column"))
for i in range(b):
    d=[]
    for j in range(c):
        e = int(input("Enter the number in the rows"))
        d.append(e)
    a.append(d)
v=np.array(a)
for i in range(b):
    for j in range(c):
        print(v[i][j],end="  ")
    print()
