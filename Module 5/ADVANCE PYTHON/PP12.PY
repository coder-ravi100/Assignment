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
try:
    number1 = int(input("Enter Number 1:"))
    number2 = int(input("Enter The Number 2:"))
    ans = number1 / number2
    print(f"Answer Is :{ans}")

except ValueError:
    print("Please Ennter Only Number")

except ZeroDivisionError:
    print("Can Not Divide By Zero")

except Exception as e:
    print("other some error occurred:",e)

else:
    print("Program Excuted Successfully")

finally:
    print("Program End") 


