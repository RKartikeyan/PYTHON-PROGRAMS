a=int(input("enter a number"))
b=a
c=0
d=0
while(b>0):
    c=b%10
    d=(d*10)+c
    b=b//10
print(d)
if(d==a):
   print("pallindrome")
else:
   print("NAHI REY")

