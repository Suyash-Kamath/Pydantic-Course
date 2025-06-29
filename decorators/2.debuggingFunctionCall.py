# Create a Decorator to print the function name and the values of its arguments every time the function is called

# Remember , formatted strings me None nahi aata hai

def debug(func):
    # Jitne bhi args aaye wo lelo , and jitne bhi key value pairs aayi hai wo bhi lelo
    def wrapper(*args,**kargs):
        # join method gives iterable list , the moment you use join() , you get iterable and you can use comprehension in join
        args_value =', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"${key}={value}" for key,value in kargs.items())
        print(f"calling : {func.__name__} with args {args_value} and {kwargs_value} kwargs")
        return func(*args,**kargs)

        
    return wrapper
# .items() is a built-in dictionary method that returns each key-value pair as a tuple., .items() returns a view object, not a list — and that view cannot be appended to.
@debug
def hello():
    print("Hello")

@debug    
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")

                # named parameter
hello()
greet("chai" , greeting="haanji ")