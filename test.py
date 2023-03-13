from math import factorial

def permutations(str):
    
    for permutation in range(factorial(len(str))):
        str= list(str)
        indexOfFirstValue = 0
        
        print(str)
        
        indexOfFirstValue += 1
        
        

permutations("abc")