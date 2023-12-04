def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

# Example usage:
n = 1
# n = 40
# n = 60
result = fibonacci_iterative(n)
print(f'fibonacci({n})={result}')
