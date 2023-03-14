# print("Que miras bobo")
def binarySearchRecur(array, start, end, target):
    while start <= end:
        
        mid = start + end - 1// 2
        
        
        if array[mid] < target:
            start1 = mid + 1
            return binarySearchRecur(array, start1, end, target)
            
        elif array[mid] > target:
            end1 = mid - 1
            return binarySearchRecur(array, start, end1, target)
            
        else:
            return mid
arr = [1, 2, 3, 4, 5]
print(binarySearchRecur(arr, 0, len(arr)-1, 4))