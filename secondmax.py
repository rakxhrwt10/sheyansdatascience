def second_max(nums):
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second

# Example
print(second_max([10, 20, 4, 45, 99]))