def count(n: int):
    if n==0:
        return 0
    count(n-1)
    print(n)

print(count(5))


