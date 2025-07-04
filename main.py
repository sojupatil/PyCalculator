def add(n,m):
    return n+m

def sub(n,m):
    return n-m

def multiply(n,m):
    return n*m

def divide(n,m):
    if m==0:
        return "Error : You cannot divide by Zero"
    return n/m


first = float(input("Enter First Number "))
second = float(input("Enter Second Number "))
option = input("Enter Choice:\n\nEnter add for Addition\nEnter sub for Subtraction\nEnter mul for Multiplication\nEnter div for Divide\n")

if(option == "add"):
    print(add(first,second))
elif (option == "sub"):
    print(sub(first,second))
elif (option == "mul"):
    print(multiply(first,second))
elif (option == "div"):
    print(divide(first,second))
else:
    print("Error : Invalid") 
