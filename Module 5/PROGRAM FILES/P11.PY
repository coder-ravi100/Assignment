'''
Assessment: 
• Create a mini-project where students combine conditional statements, loops, and functions 
to create a basic Python application, such as a simple calculator or a grade management 
system.
'''
num_student = int (input("Enter Total Number Of Student :")) #2

for i in range(num_student): #1 < 2
    print("\nStudent",i+1) #1.
    name = input("Enter The Student Name :")#Ravi

    marks1 = int (input("Enter Marks of Mathametics:")) #10
    marks2 = int (input("Enter marks of Science:")) #20
    marks3 = int (input("Enter Marks of Physics:")) #30

    total  = marks1 + marks2 + marks3 #10 20 30 = 60
    avg = total / 3
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail" #this block execute

print("------------------------------")
print("NAME :",name) #Ravi
print("TOTAL MARKS :",total) #60
print("AVERAGE :",avg)  #20
print("GRADE :",grade) #fail