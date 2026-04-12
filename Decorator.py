"""
Basic Syntex of Decorator:

import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

========== OR ==========
def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

Rules:
1.
2.
3.
4.
5.
"""

"""
1. Logging Decortor
"""
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} function returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(a=2,b=3))