a=input("enter a string")
vowel=0
const=0
for i in range(0,len(a)):
    if(a[i]!=""):
        if(a[i]=="a" or a[i]=="A" or a[i]=="e" or a[i]=="E" or a[i]=="i" or a[i]=="I" or a[i]=="o" or a[i]=="O" or a[i]=="u" or a[i]=="U"):
            vowel=vowel+1
        else:
            const=const+1
print("v=",vowel)
print("c=",const)