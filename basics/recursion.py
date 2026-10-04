def factorial(n) :
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)

fact = int(input("enter number to know its factorial : "))

print(f"factorial of {input} is {factorial(fact)}")

def add(n):
    if(n==0):
        return 0
    
    return n+add(n-1)

sum= int(input("enter number to sum till it : "))
print(add(sum))