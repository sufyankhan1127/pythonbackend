# use of *args to pass a variable number of arguments to a function. This allows you to handle more arguments than you specified when defining the function.
def add(*numbers):
    total=0

    for number in numbers:
        total += number
    return total

print(add(10,20,30))
print(add(10,20,30,40,50))



# use of **kwargs to pass a variable number of keyword arguments to a function. This allows you to handle named arguments that you may not have defined in advance.
def userinfo(**details):
    print(details)

userinfo(name="John", age=30, city="New York")
userinfo(name="Alice", age=25, street="123 Main St", country="USA", profession="Engineer")

# this is a simple example of a class in Python. A class is a blueprint for creating objects, and it defines the attributes and methods that the objects will have. In this example, we define a class called User with two attributes: name and age. We also define an __init__ method that initializes these attributes when a new instance of the class is created.
# encapsulation implemented here, as the attributes of the class are encapsulated within the class and can only be accessed through the methods of the class. This allows us to control how the attributes are accessed and modified, and helps to prevent unintended changes to the state of the object.


class User:
    def __init__(self, name, age):
        # we use __init__ method to initialize the attributes of the class. The self parameter refers to the instance of the class and allows us to access its attributes and methods.
        self.name = name
        self.age = age

User1 = User("Sufyan", 23)
print("Username is :",User1.name,"age is :", User1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add(self, a, b):
        return a + b

person1 = Person("Alice", 25)
print("Name:", person1.name)
print(person1.add(10, 20))


# this is inheritance in python. Inheritance is a mechanism that allows you to create a new class based on an existing class. The new class inherits the attributes and methods of the existing class, and can also have its own attributes and methods. In this example, we define a base class called Animal with a method called speak. We then define a subclass called Cat that inherits from the Animal class and adds its own method called meows. When we create an instance of the Cat class, we can call both the speak method inherited from the Animal class and the meows method specific to the Cat class.
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def meows(self):
        print("Cat meows")

cat = Cat()
cat.speak()  # Inherited method from Animal class
cat.meows()  # Method specific to Cat class


class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog=Dog()
dog.speak()  # Overridden method from Dog class

# exception handling is a mechanism that allows you to handle errors and exceptions that may occur during the execution of your code. In this example, we use a try-except block to catch a ZeroDivisionError that may occur when dividing by zero. If the user enters zero as the input, the program will print an error message instead of crashing.
try:

    a=int(input("Enter the number: "))
    c=10/a
    print("The result is: ",c)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exception occurred.")


# file handling is a mechanism that allows you to read from and write to files in Python. In this example, we use the open() function to open a file called test.txt in read mode. We then use the read() method to read the contents of the file and print it to the console. Finally, we close the file using the close() method to free up system resources.
# file=open("test.txt","w")
# file.write("Hello, this is a test file.\n")
# file.close()

file=open("test.txt","r")
data=file.read()
print(data)
file.close()


with open("test.txt", "r") as file:
    data = file.read()
    print(data)


# type hints are a feature in Python that allow you to specify the expected data types of function arguments and return values. This can help improve code readability and catch potential errors during development. In this example, we define a function called add1 that takes two integer arguments and returns an integer result. The type hints indicate that both a and b should be integers, and the return value should also be an integer.
def add1(a:int, b:int) -> int:
    return a + b


# asyncio in Python is a library that provides support for asynchronous programming. It allows you to write concurrent code using the async/await syntax, which can help improve the performance of I/O-bound tasks by allowing other tasks to run while waiting for I/O operations to complete. In this example, we define an asynchronous function called greet that prints "Hello, World!" to the console. We then use asyncio.run() to run the greet coroutine, which will execute the function and print the message.
import asyncio

async def greet():
    print("Hello, World!")

# print("Before calling greet()")
# greet()  # This will not run the coroutine, it will just create a coroutine object
print("After calling greet()")
asyncio.run(greet())

import asyncio

async def greet():
    print("Starting")

    await asyncio.sleep(2)

    print("Finished")


asyncio.run(greet())


async def task1():
    await asyncio.sleep(2)
    print("Task 1 finished")


async def task2():
    await asyncio.sleep(1)
    print("Task 2 finished")


async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())


# context manager
# yeild
# decorators
# generators
# environment variables


def decorator(func):
    def wrapper():
        print("before decorator")
        func()
        print("after decorator")
    return wrapper


@decorator
def my_function():
    print("Hello, World!")


my_function()