import numpy as np
a=[]
b=int(input("enter the size of the array"))
for i in range (b):
    c=int(input("enter elements in array"))
    a.append(c)
d=np.array(a)
for i in range(d.size):
    print(d[i])
sum=0
for i in range(d.size):
    sum=sum+d[i]
print(sum)
d=d[:6]
print(d)


