#7.WORKING WITH DICTIONARIES

#1.Write a Python program to update a value in a dictionary. 
dict = {"name":"Ravi","City":"Modasa","Number":9316168976}
update_name = dict["name"] = "Shyaam"
print(update_name)
print(dict)


#2.Write a Python program to merge two lists into one dictionary using a loop. 
keys = ["Name","Age","City"]
values = ["Ravi",25,"Modasa"]
empty_dict = {}

for i in range(len(keys)):
    empty_dict[keys[i]] = values[i]

print(empty_dict)


#Practical Examples: 
#(15) Write a Python program to update a value at a particular key in a dictionary. 
keys = {"name":"Ravi","Age":25,"City":"Modasa"}
#print(keys)
keys["City"] = "Ahmedabad"
print(keys)


#(16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.
my_dict = {"name":"Ravi","Age":25,"City":"Modasa"}

key_lst = list(my_dict.keys())
value_lst = list(my_dict.values())

print("Keys:",key_lst)
print("Values:",value_lst)


#(17) Write a Python program to convert two lists into one dictionary using a for loop. 
keys = ["Name","Age","City"]
values = ["Ravi",25,"Modasa"]
empty_dict = {}

for i in range(len(keys)):
    empty_dict[keys[i]] = values[i]

print(empty_dict)


#(18) Write a Python program to count how many times each character appears in a string.

text = "Python Language"
char_count = {}
for i in text:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)