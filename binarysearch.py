def BinarySearch(lst, target):
    i = 0
    j = len(lst) - 1

    while i <= j:
        mid = (i + j) // 2

        if lst[mid] == target:
            return True
        
        elif lst[mid] < target:
            i = mid + 1
        
        else:
            j = mid - 1

    return False
print(BinarySearch([1,2,3,4,5,6],6))