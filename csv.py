import csv
def create():
    with open("kartikeyan.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(["Rollno","Name","Marks"])
        while True:
            Rollno=int(input("enter a number"))
            Name=(input("enter the name"))
            Marks=int(input("Enter the Marks"))
            rec=[Rollno,Name,Marks]
            fobj.writerow(rec)
            ch=int(input("1->enter more,2->Done"))
            if(ch==2):
                break:

def display():
    with open("kartikeyan.csv","r")as obj:
        fobj=csv.reader(obj)
        for i in fobj:
            print(i)
def searching():
    with open("kartikeyan.csv","r")as obj:
        fobj=csv.reader(obj)
        next.fobj
        for i in fobj:
            if(i[2]>75):
                print(i)
                x=x+1
            if(x==0):
                print("data not found")


