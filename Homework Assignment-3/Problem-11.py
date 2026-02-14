def trap_rainwater(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0
    
    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1
    
    return water


# Example test cases
test_cases = [
    [3, 0, 1, 0, 4, 0, 2],
    [3, 0, 2, 0, 4],
    [1, 2, 3, 4],
    [2, 1, 5, 3, 1, 0, 4]
]

for arr in test_cases:
    print("Input:", arr)
    print("Water trapped:", trap_rainwater(arr))
    print("-" * 30)
