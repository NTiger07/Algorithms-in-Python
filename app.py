# print("Que miras bobo")

def factorialTrial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial
        
print(factorialTrial(5))