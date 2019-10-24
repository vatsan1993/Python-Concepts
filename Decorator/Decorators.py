# Decorators are used to add functionality to a function without changing the code of a function.
# If needed we can use the decorator on different functions . Like routes in flask and loggers
# the wraps from the functtools will remove te conflicts with multiple decorators
from functools import wraps

def my_function_decorator(orig_funct):
    @wraps(orig_funct)
    def wrapper(*args, **kwargs):
        print("Added functionality")
        return orig_funct(*args, **kwargs) # calling the original function and returning result
    return wrapper # returning the wrapper without calling


class my_decorator(object):
    def __init__(self, orginal_function):
        self.original_function=orginal_function

    def __call__(self, *args, **kwargs):
        #added functionality
        print("Functionality that will be added before the original function")
        return self.original_function(*args, **kwargs)

@my_decorator
def my_original_function():
    print("This is the code for the original Function")

@my_decorator
def my_second_original_function(name, age):
    print("This is the code for the second original Function that takes arguments.")

my_original_function()

my_second_original_function("srivatsan", 20)


# decorator function that receives parameter like flask route
def my_argument_decorator(arg):
    def my_function_decorator(orig_funct):
        @wraps(orig_funct)
        def wrapper(*args, **kwargs):
            print()
            print("Added functionality")
            print("The wrapper can now use the arguments given to the top most decorator")
            return orig_funct(*args, **kwargs) # calling the original function and returning result
        return wrapper # returning the wrapper without calling
    return my_function_decorator

@my_argument_decorator("Srivatsan")
def myargumentDecExample():
    print("Ny bormal function")


myargumentDecExample()