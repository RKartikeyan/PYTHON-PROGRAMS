def gcd(a,b):
    if(a==1):
        return b
    else:
        return (gcd(b%a,b))
a=int(input("no."))
b=int(input("no."))
print(gcd(a,b))

