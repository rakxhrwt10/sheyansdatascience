def rotateLeft(arr):
    if len(arr) == 0: return arr
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

def ro(lst:list):
    if len(lst)==0 :return lst
    temp=lst[0]
    for s in range(1,len(lst)):
        lst[s-1]=lst[s]
    lst[len(lst)-1]=temp
    return lst

print(ro([1,2,3,4,5]))
print(rotateLeft([10,20,30,40,50]))

