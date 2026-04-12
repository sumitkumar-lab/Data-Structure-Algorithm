"""
find subset: backtracking method
"""

def subset(arr, ans, i):
    if i==len(arr):
        return print(ans)
    
    ans.append(arr[i])
    subset(arr, ans, i+1)
    ans.pop()
    subset(arr, ans, i+1)


array = [1,2,3]
answer = []
print(subset(array, answer, 0))