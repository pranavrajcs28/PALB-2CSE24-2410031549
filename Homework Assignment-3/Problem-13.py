def is_subset(a, b):
    # Dictionary to store frequency of elements in array a
    freq = {}
    
    # Count elements of a[]
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    # Check elements of b[]
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True


# Example test cases
test_cases = [
    ([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]),
    ([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]),
    ([10, 5, 2, 23, 19], [19, 5, 3])
]

for a, b in test_cases:
    print("Array a:", a)
    print("Array b:", b)
    print("Is b subset of a?:", is_subset(a, b))
    print("-" * 40)
