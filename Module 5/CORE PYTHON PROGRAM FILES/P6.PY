#6.GENERATORS AND ITERATORS

#1.Write a generator function that generates the first 10 even numbers.

def Generator_Square(lst):
    for i in lst:
        yield i * i

lst = [1,2,3,4,5,6,7,8,9,10]
gen = Generator_Square(lst)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))    


#2.Write a Python program that uses a custom iterator to iterate over a list of integers. 

def my_iterator(data):
    for i in data:
        yield i #one by one return karta hai 

nums = [10,20,30,40]
for f in my_iterator(nums):
    print(f)

        

