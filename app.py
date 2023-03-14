# print("Que miras bobo")
def binarySearchRecur(array:list, target:int):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if array[mid] < target:
            start = mid + 1
            binarySearchRecur(array, target)
            
        elif array[mid] > target:
            end = mid - 1
            binarySearchRecur(array, target)
            
        else:
            return mid
    return start

print(binarySearchRecur([1, 2, 3, 4, 5], 4))