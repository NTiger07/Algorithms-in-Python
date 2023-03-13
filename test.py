from math import factorial

def permutations(str):
    
    for permutation in range(factorial(len(str))):
        str= list(str)
        print(str)
        
        indexOfLastValue = len(str) - 1
        
        while len(str) >= 2 and str[indexOfLastValue - 1] > str[indexOfLastValue]:
            indexOfLastValue -= 1
        
        
        

permutations("abc")