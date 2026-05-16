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