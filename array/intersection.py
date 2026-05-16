def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for i in nums1:
        for j in nums2:
            if i==j:
                if i not in result:
                    result.append(i)
                
                break

    return result

# print(intersection([1,2,3,4,5], [6,2,3,8,9]))

arr1 = [1,2,3,4,5]
arr2 = [6,2,3,8,9]

result = []
for i in arr1:
    for j in arr2:
        if i == j:
            print(f"Similarity found: {i}, {j}")
            if i not in result:
                result.append(i)

            break
        else:
            print(f"not found: {i}, {j}")

# print(result)

