#5.LOOPING (FOR  WHIILE)

#1.Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

List1 = ['apple', 'banana', 'mango']
for i in List1:
    print(i) 
#2.Practical Example 2: Write a Python program to find the length of each string in List1.

List1 = ['apple', 'banana', 'mango']
for i in List1:
    print(f"{len(i)}")
#3.Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition. 

List1 = ['apple', 'banana', 'mango']

search_item = "banana"

for i in List1:
    if i == search_item:
        print(f"{search_item}:Found")
        break
else:
    print(f"{search_item}:Not Found")
#4.Practical Example 4: Print this pattern using nested for loop:
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

num = int (input("Enter Number:"))
for i in range(num):   #CONTROL ROW
    for j in range(i): #CONTROL NUMBER OF STAR ROW
        print("*",end=" ")
    print()

