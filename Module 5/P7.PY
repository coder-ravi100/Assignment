#PATTERNS
# 4. Practical Example 4: Print this pattern using nested for loop: markdown
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
