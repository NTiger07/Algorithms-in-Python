def binarySearchIter(array:list, target:int):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] < target:
            start = mid + 1
            
        elif array[mid] > target:
            end = mid - 1
            
        else:
            return mid
    return start

print(binarySearchIter([1, 2, 3, 4, 5], 4))