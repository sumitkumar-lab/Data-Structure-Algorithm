try:
    result = int(input("Give me a number: "))
except ValueError as e:       # Built in error
    print(f"Need number of integer type... {e}")


"""
Custom Error...
"""
class myerror(Exception):
    pass

try:
    raise myerror("Something went wrong")

except myerror:
    print("Handled my custom error")

"""
raise keyword: “Something is logically wrong, and I want to STOP execution immediately.”
"""
age = 5

if age < 0:
    raise ValueError("Invalid Age given, age can't be less than 0")


def division(a, b):
    if b==0:
        raise ValueError("B can't be zero")
    return a/b

print(division(2, 0))

"""
raise Exception as e
"""
import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    print(f"Attempt {attempt + 1} succeeded")
                    return result
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def call_api(prompt):
    if random.random() < 0.7:
        raise Exception("API rate limit hit")
    return f"Response to: {prompt}"

print(call_api("what is python?"))