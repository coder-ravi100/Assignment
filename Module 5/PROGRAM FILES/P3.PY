# 1. Practical Example 3: How to take user input using the input() function.
student_roll_no = int (input("Enter The Roll Number:"))
student_name = input ("Enter Your Name:")
student_age = int (input("Enter The Age:"))

print(f"Student Roll Number Is :{student_roll_no}")
print(f"Student Name :{student_name}")
print(f"Student Age :{student_age}")

print("\n")
# 2. Practical Example 4: How to check the type of a variable dynamically using type().
student_roll_no = int (input("Enter The Roll Number:"))
student_name = input ("Enter Your Name:")
student_age = int (input("Enter The Age:"))
student_per = float (input("Enter The Percentage:"))

print(f"Student Roll Number Is :{student_roll_no}")
print(f"Student Name :{type(student_name)}")
print(f"Student Age :{type(student_age)}")
print(f"Student Percentage :{type(student_per)}")

