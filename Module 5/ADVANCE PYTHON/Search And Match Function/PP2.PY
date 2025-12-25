#24)Write a Python program to match a word in a string using re.match(). 
import re

text = "Tops Technnologies"
pattern = "Tops"

result = re.match(pattern,text)

if result:
    print(f"Match Found:{result.group()}")

else:
    print("No match found")