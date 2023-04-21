a=int(input("enter a number"))
b=a
c=0
d=1
while(b>0):
    c=b%10
    d*=c
    b=b//10
print(d)

