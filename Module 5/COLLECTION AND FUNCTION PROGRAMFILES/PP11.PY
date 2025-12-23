#Practical Examples: 
#4) Write a Python program to create a file and print the string into the file.
file = open("Document2.txt","w")
data = input("Enter string To Write into file :")
file.write(data)
print("Data Return Successfully!")



print("\n")#5) Write a Python program to read a file and print the data on the console. 
file = open("C:\\Users\\Admin\\Downloads\\demo.txt","r")
data1 = file.read()
print(data1)



print("\n")#6) Write a Python program to check the current position of the file cursor using tell(). 
file = open("C:\\Users\\Admin\\Downloads\\doc1.txt","r")

print("First Position:",file.tell())

file.read(5)

print("Cursor Position After Reading 5 Characters:",file.tell())

file.close()
