from math import factorial
#NO COMPRENDO
def permutations(str):
    
    for permutation in range(factorial(len(str))):
        str= list(str) # convert to list
        print(str) # print the string
        
        index = len(str) - 1 # initial value of index is last value
        
        while len(str) >= 2 and str[index - 1] > str[index]:
            # check if the length of the string is at least 2
            # AND if the second to the last value is greater then the last value
            index -= 1 # if so, then decrement the index by 1
            
        str[index:] = reversed(str[index:]) #reverse the remaining items
        
        if index > 0: #if index is not the first element
            q = index
            while str[index - 1] > str[q]:
                q += 1
            temp = str[index - 1]
            str[index - 1] = str[q]
            str[q] = temp
        
permutations("abc")
          
