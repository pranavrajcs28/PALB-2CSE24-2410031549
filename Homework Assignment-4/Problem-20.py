import math

def merge_without_extra_space(a, b):
    n, m = len(a), len(b)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        # Compare elements in a[]
        i = 0
        while i + gap < n:
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1

        # Compare elements in a[] and b[]
        j = gap - n if gap > n else 0
        i = i if gap <= n else n
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1

        # Compare elements in b[]
        if j < m:
            j_inner = 0
            while j_inner + gap < m:
                if b[j_inner] > b[j_inner + gap]:
                    b[j_inner], b[j_inner + gap] = b[j_inner + gap], b[j_inner]
                j_inner += 1

        # Update gap
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)


# Example test cases
test_cases = [
    ([2, 4, 7, 10], [2, 3]),
    ([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]),
    ([0, 1], [2, 3])
]

for a, b in test_cases:
    print("Original a:", a)
    print("Original b:", b)
    merge_without_extra_space(a, b)
    print("Merged a:", a)
    print("Merged b:", b)
    print("-" * 50)
