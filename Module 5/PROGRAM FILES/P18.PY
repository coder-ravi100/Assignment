#6.DICTIONARIES
#1.Write a Python program to create a dictionary with 6 key-value pairs. 
bio_data = {
            "Name":"Ravi",
            "Age":26,
            "Address":"Pavan City",
            "City":"Modasa",
            "Course":"Backend Developer",
            "Score":"25%",
            "Personality":"Good"
            }

#2.Write a Python program to access values using dictionary keys. 
bio_data = {
            "Name":"Ravi",
            "Age":26,
            "Address":"Pavan City",
            "City":"Modasa",
            "Course":"Backend Developer",
            "Nationality":"Indian",
            "Personality":"Good"
            }
print(bio_data["Name"])   
print(bio_data["Age"])
print(bio_data["Address"])
print(bio_data["City"])
print(bio_data["Course"])
print(bio_data["Nationality"])
print(bio_data["Personality"])

#Practical Examples: 
#(13) Write a Python program to create a dictionary of 6 key-value pairs. 
bio_data = {
            "Name":"Ravi",
            "Age":26,
            "Address":"Pavan City",
            "City":"Modasa",
            "Course":"Backend Developer",
            "Nationality":"Indian",
            "Personality":"Good"
            }

#(14) Write a Python program to access values using keys from a dictionary.
bio_data = {
            "Name":"Ravi",
            "Age":26,
            "Address":"Pavan City",
            "City":"Modasa",
            "Course":"Backend Developer",
            "Nationality":"Indian",
            "Personality":"Good"
            }

print(bio_data.get("Name"))        
print(bio_data.get("Age"))    
print(bio_data.get("Unknown"))  
