#  Log the name and arguments of any function being called.


def log_calls(func):
    def wrapper(*args,**kwargs):
        print(f"Calling function {func.__name__} and args {args} and kwargs {kwargs}")
        return func(*args,**kwargs)
    return wrapper


@log_calls
def greet(name,age=None):
    print(f"Name: {name} and Age: {age}")

greet("Suyash",age=22)