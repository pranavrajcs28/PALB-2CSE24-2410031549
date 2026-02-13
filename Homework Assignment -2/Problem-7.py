def two_sum(nums, target):
    # Dictionary to store number and its index
    num_map = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        # If complement exists in dictionary, return indices
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number with its index
        num_map[nums[i]] = i


# Example usage
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print("Input nums:", nums)
print("Target:", target)
print("Output indices:", result)
