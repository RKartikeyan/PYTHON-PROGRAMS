k=1
n=int(input("enter a number"))
a=1
while(a<=n):
    b=1
    while(b<=(n-a)):
        print(" ",end="")
        b=b+1
    c=1
    while(c<=k):
        print("*",end="")
        c=c+1
    k=k+2
    print()
    a=a+1