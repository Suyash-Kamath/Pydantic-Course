# Write a decorator that measures the time a function takes to execute

import time

# Let's make this toll so that every function will go through this
def timer(func):
    def wrapper(*args,**kwargs):
      start = time.time()
      result =  func(*args,**kwargs)
      end = time.time() 
      print(f"{func.__name__} ran in {end-start} time")
      return result
    return wrapper


@timer # decorators hai , so whenever you call this function , then this won't get directly called , this function will go through the timer , return wrapper returns to the decorator , okay ?? , if you want to make decorator then make function inside function and inside that function runs/ gets executed
def example_func(n):
   time.sleep(n)

example_func(2)