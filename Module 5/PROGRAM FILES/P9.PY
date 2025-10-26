#9.string manipulation

#1.Write a Python program to demonstrate string slicing. 

# EXAMPLE 1:BASIC SLICING
text = "PYTHON"
print(text[0:])#output:PYTH


#EXAMPLE 2:SKIP START OR END
print(text[:4])#output:PYTH
print(text[2:])#output:THON


#EXAMPLE 3:Step Use Karna
print(text[::2])#output:PTO
print(text[1::2])#output:YHN


#EXAMPLE 4:Reverse Using Slicing
print(text[::-1]) #output:NOHTYP


#EXAMPLE 5:Negative Indexing With Slicing
print(text[-4:-1]) #output:THO


#2.Write a Python program that manipulates and prints strings using various string methods.

print()#1.LOWER
text = "PARIMAL GARDEN"
lower = text.lower()
print(lower)

print()#2.UPPER
text = "Pavan city"
upper = text.upper()
print(upper)

print()#3.TITLE
text = "tops technologies pvt"
title = text.title()
print(title)

print()#4.CAPITALIZE
text = "tops technologies pvt"
capitaliize = text.capitalize()
print(capitaliize)

print()#5.FIND
text1 = "insta millionaire"
text2 = "poor boy"
index1 = text1.find("millionaire") #RETURN THE POSITION
index2 = text.find("rich")
print(index1)
print(index2)

print()#6.LEN
text = "Tops Technologies"
print(len(text))

print()#7.COUNT
text = "tic tac tu"
count = text.count("t")
print(count)

print()#8.REPLACE
sentence = input("Enter The String :")
print(sentence)
change_text = input("which word change :")
update_text = input("Update word :")
ans = sentence.replace(change_text,update_text)
print(ans)

#9.ISDIGIT
text1 = "python"
text2 = "python123"
text3 = "python 123"
text4 = "python@123"
text5 = "123"

print(text1.isdigit())
print(text2.isdigit())
print(text3.isdigit())
print(text4.isdigit())
print(text5.isdigit())

print()#10.ISALPHA
text1 = "python"
text2 = "python123"
text3 = "python 123"
text4 = "python@123"
text5 = "123"

print(text1.isalpha())
print(text2.isalpha())
print(text3.isalpha())
print(text4.isalpha())
print(text5.isalpha())

print()#11.ISALNUM
text1 = "python"
text2 = "python123"
text3 = "python 123"
text4 = "python@123"
text5 = "123"

print(text1.isalnum()) #ALPHABET ALLOW
print(text2.isalnum()) #ALPHABET + NUM ALLOW
print(text3.isalnum()) #SPACE NOT ALLOW
print(text4.isalnum()) #SPECIAL CHAR NOT  ALLOW
print(text5.isalnum()) #NUMBER ALOOW

#12.ENDSWITH
text = "ravirathod100100@gmail.com"
email = text.endswith(".com")

if email:
    print("Valid Email Address..")
else:
    print("Invalid Email Address..")

#print(email) #True

