def RotateArray(lst):
    n = len(lst)
    
    last = lst[n-1]   # last element store
    
    for i in range(n-2, -1, -1):   # correct loop
        lst[i+1] = lst[i]
    
    lst[0] = last   # first position pe last daal
    
    return lst

# Example
print(RotateArray([1,2,3,4,5]))

