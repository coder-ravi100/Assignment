#8. Method Overloading and Overriding 
#19) Write a Python program to show method overloading. 

class sample:
    def add(self,*args):
        total = 0
        for i in args:
            sum = total+i
        return sum
        
obj = sample()

print(f"Single Number {obj.add(10)}")
print(f"Two Number Add {obj.add(10,20)}")
print(f"Three Number Add {obj.add(10,20,30)}")
print(f"Four Number Add {obj.add(10,20,30,40)}")


#20) Write a Python program to show method overriding..
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()


#method overloading means compile time polymorphism
#method overriding means run time polymorphism 