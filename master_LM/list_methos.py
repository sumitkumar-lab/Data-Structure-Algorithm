arr = [1, "Sumit", 25, "Anima", "Lamxmi", "MLE"]

arr.append("Amit")
arr.append([1,2,3])

arr.extend([10,20,30])

print(arr.pop(0))
print(arr.remove(10))

arr1 = [2,5,3,1,4,8,2,5]
print(arr1.sort())
print(arr1)

print(arr1.index(3))

print(arr1.count(2))

"""
sorted() -> the most used function in AI code.
"""
score = [0.3, 0.9, 0.6]
ranked = sorted(score, reverse=True)
print(score)
print(ranked)

predictions = [("cat", 0.9), ("dog", 0.3), ("bird", 0.7)]
ranked = sorted(predictions, key=lambda x: x[1], reverse=True)
# [("cat", 0.9), ("bird", 0.7), ("dog", 0.3)]

a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)   # what prints?

a = [3, 1, 4, 1, 5, 9, 2, 6]
a.remove(1)
print(a)