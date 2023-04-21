def rev(b,a):
    if(a==0):
        print(b[0])
    else:
        print(b[a],end="")
        rev(b,a-1)
b=input("enter a string")
a=len(b)-1
rev(b,a)
