def validate_positive(func):
    def wrapper(n):
        if n < 0:
            raise ValueError("Only positive numbers allowed")
        return func(n)
    return wrapper

@validate_positive
def square(n):
    return n * n

print(square(5))
# print(square(-3))  # This will raise an error
