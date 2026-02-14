def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    result = []

    while i < n1 and j < n2 and k < n3:
        
        # If all three elements are equal
        if arr1[i] == arr2[j] == arr3[k]:
            # Avoid duplicates in result
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            
            i += 1
            j += 1
            k += 1
        
        # Move the pointer of the smallest element
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    # If no common elements found
    if not result:
        return [-1]
    
    return result


# Example test cases
test_cases = [
    ([1, 5, 10, 20, 40, 80],
     [6, 7, 20, 80, 100],
     [3, 4, 15, 20, 30, 70, 80, 120]),

    ([1, 2, 3, 4, 5],
     [6, 7],
     [8, 9, 10]),

    ([1, 1, 1, 2, 2, 2],
     [1, 1, 2, 2, 2],
     [1, 1, 1, 1, 2, 2, 2, 2])
]

for arr1, arr2, arr3 in test_cases:
    print("arr1:", arr1)
    print("arr2:", arr2)
    print("arr3:", arr3)
    print("Common elements:", common_elements(arr1, arr2, arr3))
    print("-" * 50)
