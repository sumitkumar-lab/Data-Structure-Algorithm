
def single_num(arr):
    xor = 0
    for i in arr:
        xor = i^xor
    return xor

array = [4, 1, 2, 1,2, 4, 5]
print(single_num(array))

