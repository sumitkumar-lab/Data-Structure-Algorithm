def binarySearch(arr, tar, st, end):
    if st <= end:
        mid = st + (end - st) // 2

        if arr[mid] == tar:
            return mid
        
        elif arr[mid] > tar:
            return binarySearch(arr, tar, st, mid-1)

        else:
            return binarySearch(arr, tar, mid+1, end)

    return -1

def search(arr, tar):
    return binarySearch(arr, tar, 0, len(arr)-1)


array = [2,5,3,6,8,4]
target = 8

print(search(array, target))