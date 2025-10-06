# 1. Write a generator function that generates the first 10 even numbers.
count = 1
num = 2

while count <= 10:
    print(num)
    num += 2
    count += 1



print("\n")



# 2.  Write a Python program that uses a custom iterator to iterate over a list of integers.
nums = [10, 20, 30, 40, 50]
index = 0

while index < len(nums):
    print(nums[index])
    index += 1
