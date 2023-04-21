a=int(input("enter a number"))
b=a
count=0
while(b>0):
    b=b//10
    count=count+1
d=0
sum=0
b=a
while(b>0):
    d=b%10
    x=1
    y=1
    while(x<=count):
        y=y*d
        x=x+1
    sum=sum+y
    b=b//10
print(sum)


