#7. Inheritance 
"""
• Write Python programs to demonstrate different types of inheritance (single, multiple, 
multilevel, etc.).
"""
#single
class father:
    def show_father(self):
        print("This Is father Class")

class child(father):
    def  show_child(self):
        print("This Is Child Class")

obj = child()
obj.show_father()
obj.show_child()


print("\n")#multiple
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

print("\n")#Multiple
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


