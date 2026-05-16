"""
Two-sum

must use enumerate...
"""
def two_sum(arr, target):
    maps={}
    for idx in range(len(arr)):
        complement = target - arr[idx]
        if complement in maps:
            return maps[complement], idx
        maps[arr[idx]]=idx
    return -1

print(two_sum([5,2,11,7,14], 9))