def factorial_digits(n):
    # Compute factorial
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    
    # Convert factorial number into list of digits
    result = [int(digit) for digit in str(fact)]
    
    return result


# Example test cases
test_cases = [5, 10, 1]

for n in test_cases:
    print("Input:", n)
    print("Output:", factorial_digits(n))
    print("-" * 30)
