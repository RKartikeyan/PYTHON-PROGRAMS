def num(a):
    if(a==1):
        return 1
    else:
        return(a+num(a-1))
a=int(input("no."))
print(num(a))
