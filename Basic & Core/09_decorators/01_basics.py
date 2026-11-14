# It is used for preserve the metadata.
from functools import wraps

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator # Whaterver is coming in next line just wrapped up
def greet():
    print("Hello from decorator class.")

greet()

# __name__ dunder
# Why name of the functions is wrapper? because it is wrapped in decorator.
print(greet.__name__) # -->> wrapper




print('\n--------------------------\n')


def my_decorator(func):
    @wraps(func) # wrapper added from functools to preserve metadata of original method
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorator class.")

greet()
print(greet.__name__) # -->> greet
