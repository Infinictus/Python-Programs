x=input("enter a sentence : ")
a=0
b=0
c=0
d=1
l=len(x)
while a<10:
    print("1.Length")
    print("2.Vowel")
    print("3.Word Count")
    print("4.Change Case")
    print("5.First letter of every word capital")
    print("6.Exit")
    y=int(input("Enter your choice : "))

    if y==1:
        for i in x:
            b=b+1
        print(b)
        print()
        print("______________________________________")
        print()
    if y==2:
        for i in range(l):
            if x[i].lower()=="a" or x[i].lower()=="e" or x[i].lower()=="i" or x[i].lower()=="o" or x[i].lower()=="u": 
               c=c+1
        print(c)
        print()
        print("______________________________________")
        print()

    if y==3:
        for i in range(l):
            if x[i]==" ":
                d=d+1
        print(d)
        print()
        print("______________________________________")
        print()

    if y==4:
        for i in range(l):
            if x[i]>="A" and x[i]<="Z":
                print(x[i].lower(),end="")
            elif x[i]>="a" and x[i]<="z":
                print(x[i].upper(),end="")
            else :
                print(x[i],end="")
        print()
        print("______________________________________")
        print()
    if y==5:
        for i in range(l):
            if x[i-1]==" ":
                print(x[i].upper(),end="")
            else:
                print(x[i],end="")
        print()
        print("______________________________________")
        print()
    if y==6:
        break
            
