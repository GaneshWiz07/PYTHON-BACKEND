def add(x,y):
    return x+y
def subtract(x,y):    
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        print("Error: Division by zero is not allowed.")
        return None
def modulus(x,y):
    return x%y
def square(x):
    return x**2