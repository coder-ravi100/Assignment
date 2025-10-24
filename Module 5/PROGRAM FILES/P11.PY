# Practical Example: 1) Write a Python program to skip 'banana' in a list 
#using the continue statement. List1 = ['apple', 'banana', 'mango']
fruits = ["Apple","Banana","Mango"]
for i in fruits:
    if i == "Banana":
        continue
    print(i)



print("\n")
# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
fruits = ["Apple","Banana","Cherry","Mango"]
for i in fruits:
    if i == "Banana":
        break
    print(i)

