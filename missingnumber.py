# def missingNumbver(lst):

#     summ=0
#     n=len(lst)


#     for L in lst:


#         summ+=L

#     ans=n*(n+1)//2
    
#     return summ - ans

# print(missingNumbver([1,3,4,5,6]))


def missingNumber(lst):
    n = len(lst) + 1   # total numbers hone chahiye
    
    total_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    
    return total_sum - actual_sum

print(missingNumber([1, 2, 3, 5, 4]))
