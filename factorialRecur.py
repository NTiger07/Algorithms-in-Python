def factorialRecur(n):
    if n ==1:
        return n
    else:
        factorial = factorialRecur(n - 1)
        factorial = factorial * n
    return factorial
    
print(factorialRecur(5))