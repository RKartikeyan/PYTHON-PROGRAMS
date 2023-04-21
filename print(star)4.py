n=int(input("enter a number"))
k=(n*2)-1
a=1
while(a<=n):
    b=1
    while(b<a):
        print(" ",end="")
        b=b+1
    c=1
    while(c<=k):
        print("*",end="")
        c=c+1
    k=k-2
    print()
    a=a+1