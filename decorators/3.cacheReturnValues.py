# # Implement a Decorator that caches the return values of a function, so that when it's called with the same argument, the cached value is returned instead of re-executing the function
# import time

# def cache(func):
#     cache_value = {} # dict because accessing is very compared to array because indexing ka dhyan rakhna possible nahi , so args basis pe uska key banaye and access the value
#     print(cache_value)
#     def wrapper(*args,**kwargs):
#         if args in cache_value:
#             return cache_value[args]
#         result=func(*args)
#         cache_value[args] = result
#         return result
    
#     return wrapper


# @cache
# def long_running_function(a,b):
#     time.sleep(4) # let's say database call 
#     return a+b

# print(long_running_function(2,3))
# print(long_running_function(2,3))
# print(long_running_function(4,3))

import time

def cache(func):
  cache_values={}
  def wrapper(*args,**kwargs):
    key = (args,frozenset(kwargs.items()))
    if key in cache_values:
      return cache_values[key]
    result = func(*args,**kwargs)
    cache_values[key] = result
    return result
  return wrapper

@cache
def long_running_function(a,b):
  time.sleep(4)
  return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,b=5))
print(long_running_function(2,b=5))
print("Done")