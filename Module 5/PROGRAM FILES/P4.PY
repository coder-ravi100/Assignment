# 1. Practical Example 5: Write a Python program to find greater and less than a number using if_else.
num = int (input("Enter The Number:"))
if num > 0:
    print("The Number Is Positive")
else:
    print("The Number Is Negative")



print("\n")
# 2. Practical Example 6: Write a Python program to check if a number is prime using if_else.
num = int (input ("Enter The Number :"))
flag = 1
i = 1
while (i <= num):
    if (num % i == 0):
        flag = 1
    i+=1

if (flag == 1):
    print(num,"Is a Prime Number")
else:
    print(num,"Is a Not Prime Number")
