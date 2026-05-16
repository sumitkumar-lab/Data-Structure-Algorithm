def fibonaci(n: int):
    if n==0 or n==1:
        return n
    
    return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(6))