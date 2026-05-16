def max_subarray(arr):
    n = len(arr)
    for s in range(n):
        # e=s
        for e in range(s, n):
            subarray = []
            
            for i in range(s, e+1):
                subarray.append(arr[i])

            print(subarray)


max_subarray([1,2,3,4,5])


# def max_subarray(arr):
#     n = len(arr)

#     for s in range(n):
#         for e in range(s, n):
#             subarray = []
#             for i in range(s, e+1):
#                 subarray.append(arr[i])

#             print(subarray)

# max_subarray([1,2,3,4,5])