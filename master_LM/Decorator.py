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
# import functools

# def log_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} function with {args} {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} function returned {result}")
#         return result
#     return wrapper

# @log_calls
# def add(a, b):
#     return a + b

# print(add(a=2,b=3))

print("=========== Function to Decorator ============")

def logger(func):
    def wrapper(*arg, **kwarg):
        print(f"Calling :{func.__name__}")
        result = func(*arg, **kwarg)
        print("Done")
        return result
    return wrapper

# def add(a, b):
#     return a+b

# addition = logger(add)
# print(addition(3, 5))

@logger
def square(a):
    return a**2

print(square(5))

"""
Make a timer decorator
"""
import time

def timer(func):
    def wrapper(*arg, **kwarg):
        # print("⏲ Inference time is calculating...")
        print(f"Timer function {func.__name__} is in Action...")
        start = time.time()
        result = func(*arg, **kwarg)
        print(f"{func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())
print(slow_function.__name__)   #  --> it is a wrapper function.


# @timer
# def generate(prompt: str):
#     return prompt

# print(generate("Hello, my name is Sumit Kumar..."))

"""
Make a retry decorator...
"""
def retry(max_attempt=3):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            for attempt in range(max_attempt):
                try:
                    print(f"Call {func.__name__}")
                    return func(*arg, **kwarg)
                except Exception as e:
                    print("Looking for exception and we got one")
                    if attempt == max_attempt - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
        return wrapper
    return decorator


"""
Retry -> LLM api fails sometimes

@retry(max_attempts=3)
def call_llm_api(prompt):
    return openai.chat(prompt)
"""
@retry(max_attempt=5)
def call_llm_api(prompt: str):
    return prompt

print(call_llm_api("Hello, Here is my portfolio...")) 

"""
Caching — don't call the API twice for same prompt

@lru_cache(maxsize=100)
def get_embedding(text):
    return model.encode(text)
"""
from functools import lru_cache

@lru_cache(maxsize=100)
def get_embedding(text: str):
    embed = [ord(char) for char in text]    # simple ascii conversion for num to char ord(), for char to num chr()
    return embed

print(get_embedding("Hello!"))

print("================ Fixing @wraps =================")

# This is a real problem in production. Imagine you have 20 decorated functions and your logs show wrapper 
# everywhere — you have no idea which function actually ran.

# Fix it...
import time
from functools import wraps

def timer(func):
    @wraps(func)          # ← this line
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

print(slow_function.__name__)  # now prints "slow_function"

# Retry function in fixed form
def retry(max_attempt=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kwarg):
            for attempt in range(max_attempt):
                try:
                    print(f"Call {func.__name__}")
                    print(f"Attempt {attempt + 1} succeeded")
                    return func(*arg, **kwarg)
                except Exception as e:
                    print("Looking for exception and we got one")
                    if attempt == max_attempt - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempt=3, delay=1)
def call_api(prompt):
    import random
    if random.random() < 0.7:  # fails 70% of the time
        raise Exception("API rate limit hit")
    return f"Response to: {prompt}"

print(call_api("what is python?"))



