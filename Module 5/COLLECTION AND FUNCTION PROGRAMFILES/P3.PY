#3.WORKING WITH LIST
	
#1.Write a Python program to iterate over a list using a for loop. 

iteam = [111,222,333,444,555]
for i in iteam:
    print(i)#iterator

#2.Write a Python program to sort a list using both sort() and sorted(). 

#Ascending order
order_list = [11,17,15,18,12] 
order_list.sort() 
print("Ascending:",order_list)

#Descending Order
order_list = [11,17,15,18,12]
order_list.sort(reverse=True)
print("Descending:",order_list)

#ascending
order_list = [100,500,300,600,400]
n1 = sorted(order_list)
print("Original List:",order_list)
print("Sorted List:",n1)

#Descending
order_list = [100,500,300,600,400]
n1 = sorted(order_list,reverse=True)
print("Original List:",order_list)
print("Sorted List:",n1)

#Practical Examples: 
#(5) Write a Python program to iterate through a list and print each element. 

lst = [10,20,30,40]
for i in lst:
    print(i)

#(6) Write a Python program to insert elements into an empty list using a for loop and append(). 

lst1 = []
for i in range(1,6):
    lst1.append(i)

print(lst1)