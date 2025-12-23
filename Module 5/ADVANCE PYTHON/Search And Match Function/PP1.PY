"""
10. Search and Match Functions 
"""

#23)Write a Python program to search for a word in a string using re.search(). 

import re

text = "Tops Technologies Company"
pattern = "Company"

match = re.search(pattern,text)

if match:
    print(f"'{pattern}' found in text")

else:
    print(f"'{pattern}' not found in text")
