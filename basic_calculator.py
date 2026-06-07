#A basic calculator. 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


module_name = "Simple Math Functions Module"

if __name__ == "__main__":
    print("This module starts with mathFunction.py")  # “Run this code only when this file is executed directly, not when imported.”
else:
    print("mathFunctions.py module has been imported")



    import math as mf

def main():
    try:
      while True:

        print("Basic Calculator")
        operations = ['+', '-', '*', '/']
        operation = input("Choose operation (+, -, *, /): ")
        if operation not in operations:
            print("Error: Invalid operation.")
            continue
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = mf.add(num1, num2)
        elif operation == '-':
            result = mf.subtract(num1, num2)
        elif operation == '*':
            result = mf.multiply(num1, num2)
        elif operation == '/':
            result = mf.divide(num1, num2)
        print(f"The result is: {result}")
        print(mf.module_name)
        break
    except ValueError:
        print("Error: Cannot divide by zero.")
    except KeyboardInterrupt:
        print("\nCalculation cancelled.")


if __name__ == "__main__":
    main()