# #4.CONDITIONAL STATEMENTS

#1.Practical Example 5: Write a Python program to find greater and less than a number using if else. 

numbers = int (input("Enter The Values:"))
if numbers > 100: 
    print("The number is greater than 100")
else:
    print("The number is less than or equal to 100")

# #2.Practical Example 6: Write a Python program to check if a number is prime using if_else. 

num = int (input("Enter The Value:"))
if num <= 1:  #THIS NUMBER IS NOT PRIME
    print("The Number Is Not Prime")
elif num == 2 or num == 3 or num == 5 or num == 7: #ALSO PRIME
    print("The Number Is Prime")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0: #CHECK DIVISIBLE FOR NUM
    print("The Number Is Not Prime")
else:
    print("The Number Is Prime") 

#3.Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

percentage = int (input("Enter The Values:"))
if percentage <= 100 and percentage >= 90:
    print("A Grade")
elif percentage <= 80 and percentage >= 70:
    print("B Grade")
elif percentage <= 60 and percentage >= 50: 
    print("C Grade")
else:
    print("Fail")


#4.Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int (input("Enter The Age :"))
weight = int (input("Enter The Weight :"))

if age >= 18:
    
    if weight >= 55:
        print("You Can Donate Blood")
        #THIS LINE FOR WEIGHT MATCH
    else:
        print("You Can Not Donate Blood To Underweight")

else:#THIS LINE FOR AGE MATCH
    print("Cannot Donate Blood To Age")