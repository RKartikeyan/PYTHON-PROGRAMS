a=[]
n=int(input("enter the size"))
for i in range(n):
    b=int(input("enter"))
    a.append(b)
for k in range(1,n):
    temp=a[k]
    j=k-1
    while(j>=0 and temp<a[j]):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
print(a)
