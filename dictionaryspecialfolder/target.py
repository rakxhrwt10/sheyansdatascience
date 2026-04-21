nums = [2, 7, 11, 15]
target = 9

d = {}

for i in range(len(nums)):
    diff = target - nums[i]
    
    if diff in d:
        print(d[diff], i)
    
    d[nums[i]] = i