#8.FUNCTION
#1.Write a Python program to create a function that takes a string as input and prints it. 
def msg(name):
    print("Good Morning:",name)
msg("Ravi")
msg("Ashvin")

print("---")
#2.Write a Python program to create a calculator using functions. 
def MyAddFun(num1,num2):
    sum = num1 + num2
    return sum

def MySubFun(num1,num2):
    sub = num1 - num2
    return sub

def MyMulFun(num1,num2):
    mul = num1 * num2
    return mul

def MyDiviFun(num1,num2):
    div = num1 / num2
    return div
def MyPowFun(num1,num2):
    power = num1** num2
    return power

def MyFloorFun(num1,num2):
    floor = num1 // num2
    return floor

Add_ans = MyAddFun(10,20)
print(f"Addition :{Add_ans}")
Sub_ans = MySubFun(20,10)
print(f"Subtraction :{Sub_ans}")
Mul_ans = MyMulFun(10,20)
print(f"Multiplication :{Mul_ans}")
Div_ans = MyDiviFun(10,5)
print(f"Division :{Div_ans}")
pow_ans = MyPowFun(3,3)
print(f"Power :{pow_ans}")
floor_ans = MyFloorFun(20,10)
print(f"Floor :{floor_ans}")

print("---")
#Practical Examples: 
#19) Write a Python program to print a string using a function. 
def MytextFun(name):
    print(f"{name}:Is Crezy Language !!!")
    
MytextFun("Python")
MytextFun("C++")



#20) Write a Python program to create a parameterized function that takes two arguments and prints their sum. 
def mysumFun(num1,num2):
    add = num1 + num2
    print(f"Sum is :{num1} + {num2} is Sum is:={add}")

mysumFun(10,20)

print("---")
#21) Write a Python program to create a lambda function with one expression.
def add(num1,num2):
    return num1+num2

print(add(12,12))
ans = lambda num1,num2,num3:num1+num1+num3
print(ans(12,12,12))
    
#22) Write a Python program to create a lambda function with two expressions.
print("---")
ans = lambda num: "EVEN" if num % 2 == 0 else "ODD"
print(ans(21))
