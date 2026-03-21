def longest_consecutive(nums):
    nums.sort()

    count = 1
    longest = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            count += 1
        else:
            count = 1

        if count > longest:
            longest = count


    return longest

    
