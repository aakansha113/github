def fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""


    fib_list = [0, 1]
    while len(fib_list) < n:
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)
    return fib_list


# Generate the first 10 Fibonacci numbers
fib_numbers = fibonacci(10)
print(fib_numbers)

