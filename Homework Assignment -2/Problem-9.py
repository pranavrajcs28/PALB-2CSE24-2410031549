def max_subarray_sum(arr):
    # Initialize current sum and maximum sum
    current_sum = arr[0]
    max_sum = arr[0]
    
    # Traverse from second element
    for i in range(1, len(arr)):
        # Either extend the current subarray or start new from current element
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Example usage
arr = [2, 3, -8, 7, -1, 2, 3]

result = max_subarray_sum(arr)

print("Input array:", arr)
print("Maximum subarray sum:", result)
