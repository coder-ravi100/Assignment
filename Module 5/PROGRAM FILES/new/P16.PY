#5.accessing tuples

#1.Write a Python program to access values between index 1 and 5 in a tuple. 

tuples = ("Python","C++","C","JAVA","SQL",".Net")
print("Index 1:",tuples[1])
print("Index 2:",tuples[2])
print("Index 3:",tuples[3])
print("Index 4:",tuples[4])
print("Index 5:",tuples[5])

#2.Write a Python program to access alternate values between index 1 and 5 in a tuple. 

tuples = (100,200,300,400,500)
n1 = tuples[1:6:2]
print("alternate values between index 1 and 5 :",n1)