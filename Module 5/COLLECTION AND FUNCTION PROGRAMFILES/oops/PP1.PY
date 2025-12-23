#6. Class and Object (OOP Concepts)
#11) Write a Python program to create a class and access the properties of the class using an object. 
class sample:

    def __init__(self,name,age):
        self.name = name
        self.age = age

obj1 = sample("Ravi",25)
print(f"Name : {obj1.name} \n Age : {obj1.age}")


