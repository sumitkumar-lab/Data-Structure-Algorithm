def plus_one(num):
    n = len(num)
    for i in range(n-1, -1, -1):
        if num[i] < 9:
            num[i] += 1
            return num
        num[i] = 0
    return [1] + num

print(plus_one([1, 9, 10]))

# print([1] + [0])