import math
from functools import reduce

# Python Concepts Revision

# 1. Variables and Data Types
x = 10                # int
y = 3.14              # float
name = "Alice"        # str
is_active = True      # bool
items = [1, 2, 3]     # list
person = {"age": 25}  # dict
t = (1, 2)            # tuple
s = {1, 2, 3}         # set

# 2. Control Flow
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# 3. Loops
for item in items:
    print(item)

count = 0
while count < 3:
    print("count:", count)
    count += 1

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# 5. Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

dog = Animal("Dog")
dog.speak()

# 6. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 7. List Comprehensions
squares = [i*i for i in range(5)]
print("Squares:", squares)

# 8. File I/O
with open("sample.txt", "w") as f:
    f.write("Hello, file!")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:", content)

# 9. Modules and Imports
print("Pi:", math.pi)

# 10. Lambda Functions
add = lambda a, b: a + b
print("Lambda add:", add(2, 3))

# 11. Map, Filter, Reduce
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda a, b: a + b, nums)
print("Doubled:", doubled)
print("Evens:", evens)
print("Sum:", sum_all)

# 12. Decorators
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()

# 13. Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print("Countdown:", num)

# 14. Type Hints
def add_numbers(a: int, b: int) -> int:
    return a + b

print("Type hinted add:", add_numbers(5, 7))