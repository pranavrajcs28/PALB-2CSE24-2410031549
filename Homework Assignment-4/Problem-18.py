def min_jumps(arr):
    n = len(arr)

    # If only one element, no jumps needed
    if n == 1:
        return 0

    # If first element is 0, cannot move
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        # Update farthest reachable index
        farthest = max(farthest, i + arr[i])

        # If we reach end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

            # If we cannot move further
            if current_end <= i:
                return -1

            # If we can reach or cross last index
            if current_end >= n - 1:
                return jumps

    return -1


# Example test cases
test_cases = [
    [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],
    [1, 4, 3, 2, 6, 7],
    [0, 10, 20]
]

for arr in test_cases:
    print("Array:", arr)
    print("Minimum jumps:", min_jumps(arr))
    print("-" * 40)
