def rotate_clockwise_by_one(arr):
    n = len(arr)
    
    if n == 0:
        return arr
    
    # Store last element
    last = arr[-1]
    
    # Shift elements to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    # Place last element at first position
    arr[0] = last
    
    return arr


# Example usage
arr = [1, 2, 3, 4, 5]

print("Original array:", arr)

rotated = rotate_clockwise_by_one(arr)

print("Array after rotation:", rotated)
