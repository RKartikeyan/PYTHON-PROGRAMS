import pickle
def write():
    f=open("kartikeyan.dat","wb")
    a=[]
    while True:
        b=int(input("enter roll no"))
        c=input("enter name")
        d=int(input("enter total marks"))
        e=([b],[c],[d])
        g=int(input("for endling press 1"))
        if(g==1):
            break
        a.append(e)
        pickle.dump(a,f)
def read():
    f=open("kartikeyan.data","rb")
    k=pickle.load(f)
    for i in k:
        print(k)

def search():
    f=open("kartikeyan.data","rb")
    p=int(input("enter roll no to search"))
    j = pickle.load(f)
    for i in j:
        if(i[0]==p):
            print(p)
            flag=1
            break
    if(flag==0):
        print("not found")