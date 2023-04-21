n=int(input("Enter A Number"))
a=1
while(a<=n):
    b=1
    while(b<=(n-a)):
        print(" ",end="")
        b=b+1
    c=1
    while(c<=a):
        print("*",end="")
        c=c+1
    print()
    a=a+1