def isSorted(arr, n):
    if n==1 or n==0:
        return True
    
    return arr[n-1] >= arr[n-2] and isSorted(arr, n-1)


array = [1,2,6,4,5]
print(isSorted(array, len(array)))
