#3. Opening and Closing Files 
'''
Lab: 
• Write a Python program to open a file in write mode, write some text, 
  and then close it.
'''
with open("textFile.txt","w") as file:

    data = input("Enter string To Write into file :")
    file.write(data)
    print("Data Written Successfully")