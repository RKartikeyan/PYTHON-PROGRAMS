a=[]
n=int(input("enter the size"))
for i in range(n):
    b=int(input("enter no"))
    a.append(b)
for k in range(n):
    for j in range(0,(n-k)-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
