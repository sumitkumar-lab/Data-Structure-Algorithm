"""
Find the freequency count of a string "ritwika"
"""
from sympy import N
import collections


def freq_count(string: str) -> dict:
    count = {}
    for char in string:
        # if char in count:
        #     count[char] += 1
        # else:
        #     count[char] = 1
        count[char] = count.get(char, 0) + 1
    return count

freequency = freq_count("ritwika")
# print(freequency)

"""
Given string s = "FAANG", how do you access the letter "N" using a positive index?

Given string s = "FAANG", how do you access the letter "G" using a negative index?

How do you slice s = "Unbeatable" to get only "beat"?

How do you reverse the string s = "Python" using slicing logic only (no .reverse() method)?

What happens if you try to do s[0] = "X" on s = "Hello"? (Understand Immutability).
"""

def access_through_possitive_index(string: str) -> str:
    for char in string:
        if char == N:
            return char
        else:
            return "None"
        
acc = access_through_possitive_index("FAANG")
# print(acc)


"""
Frequency count without using collections.defaultdict(int) or collections.Counter
"""
def FreeCount(words):
    count={}
    for s in words:
    #     if s in count:
    #         count[s]+=1
    #     else:
    #         count[s]=1
    # return count
        count[s] = count.get(s, 0) + 1
    return count

data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# print(FreeCount(data))

print(collections.Counter(data))
# print(collections.defaultdict())


"""
Frequency of unique character
"""
def frequencyUniqueCount(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for idx, val in enumerate(s):
        if count[val]==1:
            return idx
        
    return -1

print(frequencyUniqueCount("leetcode"))

