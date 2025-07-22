
import time

# Decorator to log function calls
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

# Decorator to time function execution
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Stackable decorators: order matters!
@log_calls
@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

@timer
@log_calls
def slow_multiply(a, b):
    time.sleep(1)
    return a * b

if __name__ == "__main__":
    print("=== slow_add ===")
    slow_add(3, 4)

    print("\n=== slow_multiply ===")
    slow_multiply(3, 4)
