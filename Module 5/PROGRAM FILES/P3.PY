#3.CORE PYTHON CONCEPT

#1.Write a Python program to demonstrate the creation of variables and 	different data types.

#STRING  DATA-TYPE
name = "Ravi Rathore"

#INTEGER DATA-TYPE
num = 10

#FLOAT DATA-TYPE
pi = 3.14

#BOOLEAN  DATA-TYPE
is_man = True

#LIST DATA-TYPE
fruits = ["apple","Banana","Cherry","Mengo"]

#TUPLE DATA-TYPE
shape = ("Triangle","Square","Round")

#SET DATA-TYPE
set1 = {1,2,3,3} 
set2 = {1,2,4,5}
dupalicate = set1 - set2 #DUPALICATE VALUEU SHOW

#DICTIONARY DATA-TYPE
bio_data = {
    "name":"Ravi",
    "age":26,
    "course":"backend developer"
    }

#SHOW ALL DATA
print(f"{type(name)}")
print(f"{type(num)}")
print(f"{type(pi)}")
print(f"{type(is_man)}")
print(f"{type(fruits)}")
print(f"{type(shape)}")
print(f"{type(dupalicate)}")
print(f"{type(bio_data)}")

#2.Practical Example 1: How does the Python code structure work? 

# 1️.VARIABLE SECTIION
name = "Ravi"
age = 21

# 2️.PROCESSING SECTION
# PERFORM SOME SIMPLE OPERATIONS
next_year_age = age + 1

# 3️.OUTPUT SECTION
print("Name:", name)
print("Current Age:", age)
print("Age Next Year:", next_year_age)


#3.Practical Example 2: How to create variables in Python? 

#STRING  DATA-TYPE
name = "Ravi Rathore"

#INTEGER DATA-TYPE
num = 10

#FLOAT DATA-TYPE
pi = 3.14

#BOOLEAN  DATA-TYPE
is_man = True

#DISPLAY THE VARIABLE
print("NAME:",name)
print("NUMBER:",num)
print("PI:",pi)
print("IS MAN:",True)

#4.Practical Example 3: How to take user input using the input() function
#1.INTEGER INPUT
num1 = int (input("Enter Number 1:"))
num2 = int (input("Enter Number 2:"))

print(f"ADDITION IS TWO NUMBER:{num1 + num2}")

#2.FLOAT INPUT
num1 = float (input("Enter Number 1:"))
num2 = float (input("Enter Number 2:"))

print(f"ADDITION IS TWO NUMBER:{num1 + num2}")


#5.Practical Example 4: How to check the type of a variable dynamically using type().

name = "Ravi Rathore"
marks = (87,67,88,56,50)
percentage = 78.90
result_pass = True  
subject = ["MATHEMATICS","PHYSIC","ENGLISH","CHEMETRY","GEOGRAPHY"]

#SHOW DATA IN VARIABLE
print(type(name))
print(type(marks))
print(type(percentage))
print(type(result_pass))
print(type(subject))

