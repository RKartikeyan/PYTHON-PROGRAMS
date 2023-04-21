kar={}
while True:
    a=input("enter the roll and student name to terminate press q")
    if a=="q":
        break
    b,c=a.split(",")
    kar.update({b:c})
for x,y in kar.items():
    print(x,y)
z=input("enter key to search")
if z in kar:
    print(z,kar[z])
else:
    print("not found")
