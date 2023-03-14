def linearSearch(array:list, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

print(linearSearch([1, 2, 3, 4, 5], 4))