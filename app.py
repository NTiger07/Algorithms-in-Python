# print("Que miras bobo")
from math import factorial

def permutations(str):
    for permutation in range(factorial(len(str))):
    
        print(str)
        # print(" ".join(str))
        indexOfLastValue = len(str) - 1 #index of last element
        
        while len(str) >= 2 and str[indexOfLastValue - 1] > str[indexOfLastValue]:
            indexOfLastValue -= 1
            
            
        str[indexOfLastValue:] = reversed(str[indexOfLastValue:])
        
        if indexOfLastValue > 0:
            q = indexOfLastValue
            
            while str[indexOfLastValue - 1] > str[q]:
                q += 1
                
            temp = str[indexOfLastValue - 1]
            str[indexOfLastValue - 1] = str[q]
            str[q] = temp
        
s = "abc"
s = list(s)
permutations(s)
    
        
        
# permutations("Fad")
            