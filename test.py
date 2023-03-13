from math import factorial

def permutations(str):
    
    for permutation in range(factorial(len(str))):
        str= list(str) # convert to list
        print(str) # print the string
        
        indexOfLastValue = len(str) - 1 # index of last value
        
        while len(str) >= 2 and str[indexOfLastValue - 1] > str[indexOfLastValue]:
            # check if the length of the string is at least 2
            # AND if the second to the last value is greater then the last value
            indexOfLastValue -= 1 # if so, then decrement the index by 1
        
        
        

permutations("abc")