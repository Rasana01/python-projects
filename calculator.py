def add(a,b):
    return a + b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
   try:
    return a/b
   except:
     return None

def main():
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))    
    operation = input("operation(+, -, *, /): ")
    
    if operation == "+":
        print(add(a,b))
    elif operation == "-":
        print(subtract(a,b))
    elif operation == "*":
        print(multiply(a,b))
    elif operation == "/":
        while True:
            result = divide(a, b)
            if result is None:
                print("Error: Can't divide by zero!")
                a = float(input("Enter A again: "))
                b = float(input("Enter B again: "))
            else:
                print(result)
                break
            
    else:
        print("invalid opertion!")
                        
main()    
    