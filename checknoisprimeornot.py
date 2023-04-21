a=int(input("enter the no you want to check"))
b=1
count=0
while(b<=a):
    if(a%b==0):
        count=count+1
    b=b+1

if(count==2):
    print("prime")
else:
    print("nope")
