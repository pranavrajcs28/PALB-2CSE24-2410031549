import heapq

def kth_smallest(arr, k):
    # Convert list into a min heap
    heapq.heapify(arr)
    
    # Extract the smallest element k times
    for _ in range(k - 1):
        heapq.heappop(arr)
    
    # The next popped element is the kth smallest
    return heapq.heappop(arr)


# Example test cases
test_cases = [
    ([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4),
    ([7, 10, 4, 3, 20, 15], 3)
]

for arr, k in test_cases:
    print("Array:", arr)
    print("k:", k)
    print("kth smallest element:", kth_smallest(arr.copy(), k))
    print("-" * 40)
