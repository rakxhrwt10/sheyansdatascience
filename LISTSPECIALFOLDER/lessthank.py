def lessThan(arr, k):
    ans = [i for i in arr if i<k]
    return ans

print(lessThan([12,14,15,1,5,7],5))