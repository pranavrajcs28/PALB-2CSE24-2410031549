def minimize_height_difference(arr, k):
    n = len(arr)
    
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initial difference
    ans = arr[n - 1] - arr[0]
    
    # Smallest and largest after modification
    small = arr[0] + k
    big = arr[n - 1] - k
    
    # Swap if needed
    if small > big:
        small, big = big, small
    
    # Check for every middle element
    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        # If subtraction makes it negative, skip
        if subtract < 0:
            continue
        
        # Update minimum and maximum
        minimum = min(small, subtract)
        maximum = max(big, add)
        
        ans = min(ans, maximum - minimum)
    
    return ans


# Example test cases
test_cases = [
    (2, [1, 5, 8, 10]),
    (3, [3, 9, 12, 16, 20])
]

for k, arr in test_cases:
    print("Array:", arr)
    print("k:", k)
    print("Minimum difference:", minimize_height_difference(arr.copy(), k))
    print("-" * 40)
