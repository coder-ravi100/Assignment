#4.tuple

#1.Write a Python program to create a tuple with multiple data types. 
tp = (5,3.14,"Python",100,1000)

print(tp)

#2.Write a Python program to concatenate two tuples.

tp1 = (10,20,30)
tp2 = ("Ravi","Software Developer")

concatenate = tp1 + tp2

print("TUPLE 1:",tp1)
print("TUPLE 2:",tp2)
print("concatenate :",concatenate)

#Practical Examples: 
#(7) Write a Python program to convert a list into a tuple. 

lst  = [10,20,"Python","SQL"]
tuples = tuple(lst)

print(lst)
print(tuples)

#(8) Write a Python program to create a tuple with multiple data types. 

my_tuple = (10, "string", 45.6, True, "Python", 99,3.14)

print("List with multiple data types:", my_tuple)
print("Type of my_list:", type(my_tuple))

#(9) Write a Python program to concatenate two tuples into one. 

t1 = (1,2,3)
t2 = (4,5,6)
ans = t1 + t2

print("TUPLE 1:",t1)
print("TUPLE 2:",t2)
print("concatenate :",ans)

#(10) Write a Python program to access the value of the first index in a tuple.

tuples = ("Phone","Ravi","School","Laptop")
print("Index 0:",tuples[0])