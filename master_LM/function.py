def greet(name):
    return f"Hello {name}"

say_hello = greet
print(say_hello("Sumit"))

print(id(greet))
print(id(say_hello))
print(greet is say_hello)  # what do you expect?


"""
This one insight unlocks everything in Phase 2. Because if a function is just an object with an address — 
then:
--> You can store functions in a list
--> You can pass a function as an argument to another function
--> You can return a function from a function

These three abilities are what make Python functions first-class. And they are the foundation of 
decorators, callbacks, pipeline steps, and middleware in every AI framework you'll use.
"""
# Let's prove it...
def run(func, value):
    return func(value)


def square(x):
    return x**2

def sum(x):
    return x + 2

print(run(square, 5))
print(run(sum, 10))

"""
You can return a function from a function
"""
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# What do the two prints output?
# After make_multiplier(2) finishes executing, does n get destroyed?
# What is double — is it a number, a string, or something else?

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double.__closure__)
print(double.__closure__[0].cell_contents)

"""
Use in AI
"""
# 1. Configurable prompt template
def make_prompt_template(system_role):
    def build_prompt(user_input):
        return f"You are {system_role}.\nUser: {user_input}"
    return build_prompt

rag_prompt = make_prompt_template("a factual assistant who only uses provided context")
chat_prompt = make_prompt_template("a friendly conversational assistant")

print(rag_prompt("What is Python?"))
print(chat_prompt("What is Python?"))

# 2. Configurable retry logic.
def make_retry(max_attempts):
    def retry(func):
        for attempt in range(max_attempts):
            try:
                return func()
            except Exception:
                if attempt == max_attempts - 1:
                    raise
    return retry

retry_3 = make_retry(3)
retry_5 = make_retry(5)

# print(retry_3(func()))

# 3. Stateful token counter
def make_token_counter(max_tokens):
    used = [0]  # list so closure can mutate it
    def count(tokens):
        used[0] += len(tokens)
        remaining = max_tokens - used[0]
        return remaining
    return count

counter = make_token_counter(4096)
print(counter(["hello", "world"]))      # 4094 remaining
print(counter(["how", "are", "you"]))   # 4091 remaining

# =====================================
print("=========Test==========")
def make_counter():
    count = 0
    def increment():
        count += 1  # ❌ what happens here?
        return count
    return increment

counter = make_counter()
print(counter())


"""
Retry logic
"""
import time, random
def retry_with_backoff(func, retries=3, base_delay=1):
   for attempt in range(retries):
       try:
           return func()
       except Timeout:
           delay = base_delay * (2 ** attempt) + random.uniform(0.1, 0.3)
           print(f"Retrying in {delay:.2f}s...")
           time.sleep(delay)