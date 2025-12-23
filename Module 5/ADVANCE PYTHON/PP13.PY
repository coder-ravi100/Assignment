#Practical Examples: 
#7) Write a Python program to handle exceptions in a calculator.
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


#8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
try:
    file = open("sample_doc.txt","r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("file is not found")

try: 
    no1 = 10
    no2 = 0
    print(f"Division is : {no1} and {no2} is {no1 / no2}")
   
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


#9) Write a Python program to handle file exceptions and use the finally block for closing the file. 
try:
    file = None
    file = open("Mydoc.txt","r") 
    data = file.read()
    print(data)

except FileNotFoundError:
    print("File is Not Found")

finally:
    if file:
        file.close()
        print("File Closed Successfully")


#10) Write a Python program to print custom exceptions.
try:
    age = int(input("Enter Your Age:"))

    if age < 18:
        raise Exception("You Are Not Eligible For Vote")
    
    print("You Are Eligible to Vote")

except Exception as e:
    print(f"Custom Exception:{e}")