def areasq():                                   #type 1#
   s=int(input("enter side length :"))
   print(s*s)
def areacirc():
    r=int(input("enter radius :"))
    print(3.1415*r*r)
def areatri():
    b=int(input("enter base length :"))
    h=int(input("enter height :"))
    print((1/2)*b*h)
def menu():
    a=0
    while a<10:
        print("1. Area of square","2.Area of circle","3.Area of triangle","4.Exit")
        n=int(input("Enter your choice :"))
        if n==1:
          areasq()
        elif n==2:
            areacirc()
        elif n==3:
            areatri()
        else:
            break
            
menu()

def areasq(s):                                  #type 2#
   print(s*s)
def areacirc(r):
    print(3.1415*r*r)
def areatri(b,h):
    print((1/2)*b*h)
def menu():
    a=0
    while a<10:
        print("1. Area of square")
        print("2.Area of circle")
        print("3.Area of triangle")
        print("4.Exit")
        n=int(input("Enter your choice :"))
        if n==1:
          s=int(input("enter side length :"))
          areasq(s)
        elif n==2:
            r=int(input("enter radius :"))
            areacirc(r)
        elif n==3:
            b=int(input("enter base length :"))
            h=int(input("enter height :"))
            areatri(b,h)
        else:
            break
            
menu()       

