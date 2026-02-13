def min_jumps(arr):
    n = len(arr)
    
    # If array has 0 or 1 element, no jumps needed
    if n <= 1:
        return 0
    
    # If first element is 0, we can't move anywhere
    if arr[0] == 0:
        return -1
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):
        # Update the farthest reachable index
        farthest = max(farthest, i + arr[i])
        
        # When we reach the end of the current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            # If we cannot move forward
            if current_end <= i:
                return -1
            
            # If we can reach or pass the last index
            if current_end >= n - 1:
                return jumps
    
    return -1


# Example usage
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = min_jumps(arr)

print("Input:", arr)
print("Minimum number of jumps:", result)
