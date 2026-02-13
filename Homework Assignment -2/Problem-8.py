def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If target is not found, left is the correct insert position
    return left


# Example usage
nums = [1, 3, 5, 6]
target = 5

result = search_insert(nums, target)

print("Input nums:", nums)
print("Target:", target)
print("Output index:", result)
