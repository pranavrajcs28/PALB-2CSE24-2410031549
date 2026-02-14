def find_duplicate(nums):
    # Step 1: Detect cycle (Tortoise and Hare)
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Example test cases
test_cases = [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [3, 3, 3, 3, 3]
]

for nums in test_cases:
    print("Input:", nums)
    print("Duplicate number:", find_duplicate(nums))
    print("-" * 40)
