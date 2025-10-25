#2 LIST OPERATIONS:

#1.Write a Python program to add elements to a list using insert() and append(). 

append_method = ["Ahmedabad","Surat","Gandhinagar"] #last add element
append_method.append("Rajkot")
print(append_method)


insert_method = [10,20,30,40] #particular index insert Element
insert_method.insert(1,50)
print(insert_method)

#2.Write a Python program to remove elements from a list using pop() and remove().

pop_method = ["Apple","Banana","Cherry","Mango"]
pop_method.pop()
print(pop_method)#last element delete


remove_method = [1.1,2.2,3.3,4.4]
remove_method.remove(1.1)
print(remove_method)

#Practical Examples:
# (3) Write a Python program to update a list using insert() and append(). 

insert_data = [11,12,13,14,15]
print("Without Add",insert_data)
insert_data.insert(0,10)
print("With Add",insert_data)


append_data = ["Ravi","Meera","Muskan","Kunal"]
print("Without Add",append_data)
append_data.append("Ranveer")
print("With Add",append_data)

#(4) Write a Python program to remove elements from a list using pop() and remove().

pop_data = ["Table","Chair","Desk"]
print("Without Remove",pop_data)
pop_data.pop()
print("With Remove",pop_data)


remove_data = [100,200,300,400]
print("Without Remove",remove_data)
remove_data.remove(100)
print("With Remove",remove_data)

