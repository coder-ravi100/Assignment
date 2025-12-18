"""
Practical Example: 3) Write a Python program to create a file and write a string into it.
"""
with open("sample.txt","w") as file:

    data = input("Enter string To Write into file :")
    file.write(data)
    print("Data Return Successfully!")