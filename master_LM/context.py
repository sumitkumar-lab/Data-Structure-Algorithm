a = [1,2,3,4,5]

print(a[-5:])  # is important for context management
print(a[:5])

tokens = [101, 2054, 2003, 2003, 2062, 102]
print(tokens[1:-1])
print(tokens[1:])   # what and why?
print(tokens[::2])


a = [1, 2, 3, 4, 5]
a[1:3] = [20, 30, 40]  # replace 2 elements with 3
print(a)  # [1, 20, 30, 40, 4, 5]

b = [1, 2, 3, 4, 5]
b[1:3] = []  # replace 2 elements with nothing
print(b)  # what do you expect?

c = [1, 2, 3, 4, 5]
c[1:1] = [10, 20]  # replace nothing with 2 elements
print(c) 

z = [1,2,3,4]
z[1]=5
print(z)

"""
append()
extend()
insert()
pop()
remove() -> Removes only the first one, others remain same. Your model now trains on inconsistent vocab. Silent bug again.
sort()
sorted()
reverse()
index()
count()
copy()
"""
vocab = ["the", "cat", "sat", "cat", "mat"]
vocab.remove("cat")
print(vocab)  # ["the", "sat", "cat", "mat"]

# Solution
vocab = list(set(vocab))
print(vocab)

"""
**Mini Project — Build a Token Counter**

This is your first real AI tool. Built entirely from what you've learned so far — lists, slicing, methods, mental models. No libraries.

Here's the spec:
```
Given a text string:
1. Split it into tokens (words)
2. Count total tokens
3. Show top 3 most frequent tokens
4. Trim to last 10 tokens (simulate context window)
5. Remove all occurrences of stopwords: ["the", "a", "is", "in", "it"]
"""
print("========== mini project ==========")
text = "the cat sat in the mat and the cat is happy and it is a good day"


# 1. Split it into tokens (words)
tokens = text.split(" ")
print(tokens)
# 2. Count total tokens
print(len(tokens))
# 3. Show top 3 most frequent tokens
count = {}
for s in tokens:
    count[s] = count.get(s, 0) + 1

ranked = sorted(count.items(), key=lambda x: x[1] ,reverse=True)
print(ranked[:3])
# 4. Trim to last 10 tokens (simulate context window)
print(tokens[-10:])
# 5. Remove all occurrences of stopwords: ["the", "a", "is", "in", "it"]
text = "the cat sat in the mat and the cat is happy and it is a good day"
stopwords = ["the", "a", "is", "in", "it"]

filter = " ".join([word for word in text.split() if word not in stopwords])
print(filter)


