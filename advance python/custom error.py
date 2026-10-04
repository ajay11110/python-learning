a= int(input("enter first number : "))
b= int(input("enter second number : "))

if(b==0):
    raise ZeroDivisionError("can not divide by zero")

else:
    print("result is :", a/b)