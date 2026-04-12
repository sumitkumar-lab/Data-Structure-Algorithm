""" 
Two sum

"""
# O(n^2)
def twoSum(nums: list[int], target: int) -> list[int]:

    # # O(n^2)
    # size=len(nums)
    # for i in range(size):
    #     for j in range(1, size):
    #         if (nums[i] + nums[j] == target and i!=j):
    #             return i, j
            
    
    # # O(nlogn) - optimized ---- Two Pointer
    # i=0
    # j=len(nums)-1
    # nums.sort()
    # while i<=j:
    #     if (nums[i] + nums[j]) == target:
    #         return i, j
    #     elif (nums[i]+nums[j]) > target:
    #         j-=1
    #     elif (nums[i]+nums[j]) < target:
    #         i+=1
    
    # # O(n) - more optimized ----- Hash-map
    # hashmap={}
    # for i, num in enumerate(nums):
    #     complement = target - num
    #     if complement in hashmap:
    #         return hashmap[complement], i
        
    #     hashmap[num]=i

    pass

if __name__ == "__main__":
    print(twoSum([4,2,5,6,8], target=8))


"""
Haash map
"""
nums = [2, 7, 5, 9], target = 9
hashmap = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
        print(hashmap[complement], i)
    
    hashmap[num] = i

"""
Two pointer
"""
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left<right:
        total = nums[left] + nums[right]
        if total==target:
            return (left, right)
        elif total>target:
            right-=1
        else:
            left+=1
    
    return -1


    # Hint 2: You will need an if/elif/else block for the three possible scenarios 
    #         (sum == target, sum < target, sum > target).