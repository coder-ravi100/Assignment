"""
5.Exception Handling
"""
#• Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    print("Division:", num1 / num2)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid integer values")

except Exception as e:
    print("Unexpected Error:", e)

#• Write a Python program to demonstrate handling multiple exceptions. 