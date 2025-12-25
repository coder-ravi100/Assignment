#12) Write a Python program to demonstrate the use of local and global variables in a class.

#global Variables
myname = 'ravi'
myage = 25
class sample:

   #local Variables
   def myfun(self):
    name = "Shyam"
    age = 26
      
    print(f"Local-->My Name Is:{name}")
    print(f"Local-->My Age Is :{age}")

    print(f"Global-->My Name Is:{myname}")
    print(f"Global-->My Age Is :{myage}")

obj1 = sample()
obj1.myfun()





              