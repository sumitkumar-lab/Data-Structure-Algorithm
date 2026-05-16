def unique_number(arr):
    hash = {}
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    unique_num = []
    for key, value in hash.items():
        if value == 1:
            unique_num.append(key)
    
    return unique_num
        
# print(unique_number([4,1,2,1,2,5]))



def more_unique(arr):
    for i in arr:
        ct = arr.count(i)
        if (ct%2!=0):
            print(i)

# more_unique([4,1,2,1,2,5])


# def unique_num(arr):
#     hash = {}

#     for i in hash:
#         hash[i] = hash.get(i, 0) + 1


#     return [key for key, value in hash.items() if value == 1]


# print(unique_num([4,1,2,1,2,5,6]))