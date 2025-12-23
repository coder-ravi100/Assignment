#Inheritance
#13) Write a Python program to show single inheritance. 

class father:
    def show_father(self):
        print("This Is father Class")

class child(father):
    def  show_child(self):
        print("This Is Child Class")

obj = child()
obj.show_father()
obj.show_child()


#14) Write a Python program to show multilevel inheritance. 

class Grandparent:
    def show_gp(self):
        print("This Is GrandParent Class")

class parent(Grandparent):
    def show_parent(self):
        print("This Is Parent Class")

class childs(parent):
    def show_childs(self):
        print("This is Child Class")

obj = childs()
obj.show_gp()
obj.show_parent()
obj.show_childs()


#15) Write a Python program to show multiple inheritance.
class A:
    def display_A(self):
        print("this is Base Class A")

class B:
    def display_B(self):
        print("This Is Base Class B")

class C(A,B):
    def display_C(self):
        print("this is a Derived Class C")

obj = C()
obj.display_A()
obj.display_B()
obj.display_C()


#16) Write a Python program to show hierarchical inheritance. 
class base_class:
    def show_base(self):
        print("This Is Parent Class")

class child_1(base_class):
    def show_child1(self):
        print("This Is Child-1 Class")

class child_2(base_class):
    def show_child2(self):
        print("This Is Child-2 Class")

obj1 = child_1()
obj2 = child_2()

obj1.show_base()
obj1.show_child1()

obj2.show_base()
obj2.show_child2()

#17) Write a Python program to show hybrid inheritance. 
# class GrandParent:
#     def show_Gp(self):
#         print("This Is Grand Parent Class")

# class Parent(GrandParent):
#     def show_parent(self):
#         print("This Is Parent Class")

# class Child1(Parent):
#     def show_child1(self):
#         print("This Is Child1 Class")

# class Child2(Parent):
#     def show_child2(self):
#         print("This Is Child2 Class")

# class GrandChild(Child1, Child2):
#     def show_grandChild(self):
#         print("This Is Grand Child Class")

# obj = GrandChild()
# obj.show_Gp()
# obj.show_parent()
# obj.show_child1()
# obj.show_child2()
# obj.show_grandChild()


#18) Write a Python program to demonstrate the use of super() in inheritance.
class Parent:
    def show(self):
        print("This Is Parent Class")

class child(Parent):
    def show(self):
        super().show() #parent Method Call
        print("This Is Child Class")


obj = child()
obj.show()