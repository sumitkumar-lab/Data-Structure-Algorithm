def dot_product(vec_a, vec_b):
    total=0

    # z = list(zip(vec_a, vec_b))
    # for i in z:
    #     total+=i[0]*i[1]

    # or using zip() unpack ...
    # for a, b, in zip(vec_a, vec_b):
    #     total+=a*b

    # or using sum() ...
    return sum(a*b for a, b in zip(vec_a, vec_b))

    # return total




vec_a = [1,2,3]
vec_b = [4,5,6]

print(dot_product(vec_a, vec_b))


