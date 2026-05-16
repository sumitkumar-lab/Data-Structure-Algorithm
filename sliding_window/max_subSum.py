def max_subArraySum(arr, k):

    if len(arr) < k:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):

        add_new = arr[i]
        remove_pre = arr[i-k]

        window_sum = window_sum + add_new - remove_pre
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_subArraySum([2, 1, 5, 1, 3, 2], 3))



# window_sum += arr[i]
# window_sum -= arr[i-k]

# max_sum = max(max_sum, window_sum)