# Grade Management System using loop for multiple students
num_student = int (input("Enter Total Number Of Students:"))

for i in range(num_student):
    print("\nStudent",i+1)
    name = input("Enter Student Name:")

    marks1 = int(input("Enter Marks Of Subject 1:"))
    marks2 = int(input("Enter Marks Of Subject 2:"))
    marks3 = int(input("Enter Marks Of Subject 3:"))

    total = marks1 + marks2 + marks3
    average = total / 3

    if average >=90:
        grade = "A"
    elif average >=75:
        grade = "B"
    elif average >=50:
        grade = "C"
    else:
        grade = "Fail"

print(".......................")
print("Name:",name)
print("Total Marks:",total)
print("Average:",average)
print("Grade:",grade)    
