#6.GENERATORS AND ITERATORS

#1.Write a generator function that generates the first 10 even numbers.

def Generator_Square(lst):
    for i in lst:
        yield i * i

lst = [1,2,3,4,5]
gen = Generator_Square(lst)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))    


#2.Write a Python program that uses a custom iterator to iterate over a list of integers. 
class MyIiterator:
    def __init__(self,lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.lst):
            value = self.lst[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
        
numbers = [10,20,30,40]

obj = MyIiterator(numbers)

for num in obj:
    print(num)
        

