x=int(input("Enter a number : "))
a=0
while a<10:
    print("1.Binary Equivalent")
    print("2.Octal Equivalent")
    print("3.Hexal Equivalent")
    print("4.Exit")
    y=int(input("Enter your choice : "))
z=[]
s=""
if y==1:
    for i in range(100):
         r=x%2
         q=x//2
         x=q
         z.append(r)
         if x<1:
             break
         z.reverse()
   
   l=len(z)
   for i in range(l):
       s=s+str(z[i])
   print("(",s,")",chr(0x2082),sep="")

elif y==2:
    for i in range(100):
    r=x%8
    q=x//8
    x=q
    z.append(r)
    if x<1:
        break
z.reverse()
l=len(z)
for i in range(l):
    s=s+str(z[i])
print("(",s,")",sep="")

elif y==3:
    for i in range(100):
    r=x%16
    q=x//16
    x=q
    z.append(r)
    if x<1:
        break
for k in range(len(z)):
    if z[k]==10:
        s= s+str(A)
    elif z[k]==11:
        s= s+str(B)
    elif z[k]==12:
        s= s+str(C)
    elif z[k]==13:
        s= s+str(D)
    elif z[k]==14:
        s= s+str(E)
    elif z[k]==10:
        s= s+str(F)
    else:
        s=s+str(y[k])
z.reverse()
l=len(z)
for j in range(l):
    s=s+str(z[j])
print("(",s,")",sep="")

elif y==4:
    break




