#* MODULES 14:PYTHON - COLLECTION, FUNCTIONS AND MODULES

#ACCESSING

 #1 LIST:

#1.Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.). 

my_list = [10, "string", 45.6, True, "Python", 99,3.14]

print("List with multiple data types:", my_list)
print("Type of my_list:", type(my_list))

#2.Write a Python program to access elements at different index positions.

fruits = ['Banana','Apple','Cherry','Mengo']
print(f"Index 0:{fruits[0]}")
print(f"Index 1:{fruits[1]}")
print(f"Index 2:{fruits[2]}")
print(f"Index 3:{fruits[3]}")

#Practical Examples: 
#(1). Write a Python program to create a list of multiple data type elements.

my_list = [10, "string", 45.6, True, "Python", 99,3.14]
print("List with multiple data types:", my_list)

#(2).Write a Python program to find the length of a list using the len() function. 

animal = ["lion","tiger","Chita","Hourse"]
ans = len(animal)

print("Length of the list:", ans)