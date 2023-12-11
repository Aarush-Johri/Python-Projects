a=0
b=0
def add (a,b):
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    s= a+b
    print(s)

def mul (a,b):
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    m= a*b
    print(m)

def div (a,b):
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    x= a/b
    print(x)

def sub (a,b):
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    y= a-b
    print(y)

def exp (a,b):
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    z= a**b
    print(z)

def usr_int ():
    print("Please select the operator you want to use: ")
    a = int(input("1 to 5: 1=addition, 2=multiplication, 3=substraction, 4=divide, 5=exponent: "))
    if a==1:
        add (a, b)
        return
    elif a==2:
        mul (a, b)
        return
    elif a==3:
        sub (a, b)
        return
    elif a==4:
        div (a, b)
        return
    elif a==5:
        exp (a, b)
        return

usr_int()