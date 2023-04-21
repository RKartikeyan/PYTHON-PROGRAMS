def kar(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    else:
        return(kar(n-1)+kar(n-2))
n=int(input("no."))
for i in range (1,n+1):
    print(kar(i))
