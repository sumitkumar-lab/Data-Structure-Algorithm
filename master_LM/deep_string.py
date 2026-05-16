"""
Difference between text.split() or text.split(" ")
"""
# text = "the cat sat in the mat and the cat is happy and it is a good day"

text1 = "the  cat  sat"   # double spaces
print(text1.split())      # what do you get?
print(text1.split(" "))   # what do you get?

text2 = "  hello world  "  # leading and trailing spaces
print(text2.split())       # what do you get?
print(text2.split(" "))    # what do you get?

"""
Ans:
['the', 'cat', 'sat']
['the', '', 'cat', '', 'sat']
['hello', 'world']
['', '', 'hello', 'world', '', '']
"""
"""
You already know strings are immutable. But here is what most people don't think about:
Every string operation you call — split(), strip(), replace(), upper() 
— never modifies the original. It always returns a new string.

String Methods:
strip() -> remove the spaces.
lower() -> This bring text lower case latter.
replace() -> replace text from another text.
split() -> separate every text in the string from space.
join() -> join two different strings or text.
startswith() -> text.startswith("User:")
endswith() -> text.endswith("?")
format() -> formate sentence taking variable inside { }.
f-strings -> form sentence like format() 
find() ->
"""


# Example:
conversation = ("User: What is ML ?",
                "Assistant: ML is ....")

def process_user_message(text):
    print("I'm an user, and I'm working fine...")

def process_assistant_message(text):
    print("I'm an assistant, and I'm working fine...")


for line in conversation:
    if line.startswith("User:"):
        process_user_message(line)
    elif line.startswith("Assistant:"):
        process_assistant_message(line)

"""
find() -> Returns the index of the first occurrence of a substring. Returns -1 if not found
"""
text = "The answer is: Paris"
idx = text.find(":")
print(idx)           # 14
print(text[idx+2:])  # "Paris" — extract everything after ": "

# In AI this is used to parse structured LLM outputs:
response = "Answer: The capital is Paris. Confidence: 0.95"
answer_start = response.find("Answer:") + len("Answer: ")
# print(answer_start)
# confidence_start = response.find("Confidence:") + len("Confidence: ")
answer = response[answer_start:response.find("Confidence:") - 1]
print(answer)
# confidence = response[confidence_start:]

"""
joinn()
"""
words = ["the", "cat", "sat"]
" ".join(words)     # "the cat sat"
", ".join(words)    # "the, cat, sat"
"".join(words)      # "thecatsat"

"""
format()
"""
model = "gpt-4"
tokens = 1250

# Old way
print("Model: {}, Tokens used: {}".format(model, tokens))

# Modern way — always use this
print(f"Model: {model}, Tokens used: {tokens}")

# f-strings can also do expressions inline
print(f"Cost: ${tokens * 0.002:.4f}")  # :.4f means 4 decimal places

"""
f-strings -> used for prompt building in AI engineering.
"""
def build_prompt(context: str, question: str):
    return f"""You are a helpful assistant.

    Context: {context}

    Question: {question}

    Answer:"""

context = "Hey, you are a software enginner."
question = "What is Machine Learning ?"
print(build_prompt(context, question))

def vibe_prompt(goal: str, input: str, feature: str, output: str, *args, **kwargs):
    return f"""You are a senior software engineer.

    Goal: {goal}

    Input: {input}

    Feature: {feature}

    Output: {output}

    Answer:"""

"""
strip() -> removes from both ends only, not from the middle:
"""
"the  cat  sat".strip()  # "the  cat  sat" — middle spaces untouched

"  hello  ".strip()     # "hello" — removes leading and trailing whitespace
"  hello  ".lstrip()    # "hello  " — left only
"  hello  ".rstrip()    # "  hello" — right only
"xxhelloxx".strip("x")  # "hello" — strips specific characters

"""
Q. Build a prompt cleaner...

In production LLM apps, user inputs arrive messy. Write a function that:

Strips leading and trailing whitespace
Converts to lowercase
Replaces multiple spaces with single space — hint: " ".join(text.split())
Removes the word "please" — LLMs don't need politeness tokens, it wastes context
Returns the cleaned prompt
"""
user_input = "  Please    tell me WHAT is the    capital of France?  "
# expected output: "tell me what is the capital of france?"

def clean_prompt(user_input: str):
    user_input = user_input.strip()
    user_input = user_input.lower()
    user_input = " ".join(user_input.split())
    if user_input.startswith("please "):
        user_input = user_input[len("please "):]

    return answer

print(clean_prompt(user_input))