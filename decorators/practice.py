import time 

def log_calls(func):
    def wrapper(*args,**kwargs):
        print(f"[LOG] Calling function name: {func.__name__} with arguments {args} and {kwargs}" )
        result = func(*args,**kwargs)
        print(f"[LOG] Function {func.__name__} returned {result}")
        return result
    return wrapper


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"[TIMER] Execution time of the function {func.__name__} is {end-start:.4f}")
        return result
    return wrapper
    
@log_calls
@timer
def slow_add(a,b):
    time.sleep(1)
    return a+b

@timer
@log_calls
def slow_multiply(a,b):
    time.sleep(1)
    return a*b

if __name__=="__main__":
    print("====slow add====")
    slow_add(3,4)
    print("====slow multiply====")
    slow_multiply(3,4)