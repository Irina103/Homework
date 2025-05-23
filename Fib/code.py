def fibonacci(n):
    # Base case: fibonacci(0) is 0
    if n == 0:
        return 0
    # Base case: fibonacci(1) is 1
    if n == 1:
        return 1
    # Recursive step: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example: fibonacci(5) will calculate:
# recursion 1: n = 5, fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
# recursion 2: n = 4, fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
# recursion 3: n = 3, fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
# recursion 4: n = 2, fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
# ... continues down to base cases
