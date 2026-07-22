# Decorator function
def greeting_decorator(func):
    def wrapper():
        print("----- Program Started -----")
        func()
        print("----- Program Ended -----")
    return wrapper

# Function to decorate
@greeting_decorator
def greet():
    print("Hello, Welcome to Python Decorators!")

# Calling the decorated function
greet()

def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper

def hash_line(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

@star
@hash_line
def display():
    print("Python")

display()
