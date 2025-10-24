
# 3. Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.
per = float (input("Enter The Percentage:"))

if per >= 90:
    print(f"Grade A:{per}")
elif per >= 80:
    print(f"Grade B:{per}")
elif per >= 70:
    print(f"Grade C:{per}")
elif per  >= 50 and per <= 60:
    print(f"Grade D:{per}") 
else:
    print(f"Fail")



print("\n")
# 4. Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.
age = int (input ("Enter The Age :"))
weight = int (input ("Enter The Weight :"))

if age >= 18:

    if weight >=55:

        print("You can Donate Blood")

    else: #THIS LINE FOR WEIGHT MATCH

        print("Cannot Donate Blood Due To Underweight")

else: #THIS LINE FOR AGE MATCH

    print("Cannot Donate Blood Due To Age")