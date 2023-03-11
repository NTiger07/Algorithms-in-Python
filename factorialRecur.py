def factorialRecur(n):
    if n == 1: return n
    else: return n * factorialRecur(n - 1)
    
print(factorialRecur(5))