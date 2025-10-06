                                                #LIST
# 1. Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']
fruits = ["Apple","Banana","Graps"]
for i in fruits:
    print(i)


print("\n")


# 2. Practical Example 2: Write a Python program to find the length of each string in List1.
cities = ["Ahmedabad","Surat","Rajkot","Modasa"]
for i in cities:
    print(f"{(len(i))}")


print("\n")


# 3. Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.
furniture = ["table","chair","caboard"]
search_furniture = input("Enter The Furniture:")
for i in furniture:
    if i == search_furniture:
        print(f"{search_furniture} is Available in List")


