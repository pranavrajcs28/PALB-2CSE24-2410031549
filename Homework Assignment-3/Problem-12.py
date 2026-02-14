def has_triplet_with_sum(arr, target):
    n = len(arr)
    
    # Sort the array
    arr.sort()
    
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return False



test_cases = [
    ([1, 4, 45, 6, 10, 8], 13),
    ([1, 2, 4, 3, 6, 7], 10),
    ([40, 20, 10, 3, 6, 7], 24)
]

for arr, target in test_cases:
    print("Array:", arr)
    print("Target:", target)
    print("Triplet Exists:", has_triplet_with_sum(arr, target))
    print("-" * 35)
