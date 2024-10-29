#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    if (n <= 1) or (not isinstance(n, int)):
        return 0

    operations = 0
    divisor = 2  # Start from the smallest possible divisor

    # Divide n by its smallest factors to get the minimum operations
    while n > 1:
        while n % divisor == 0:  # Check if current divisor is a factor of n
            operations += divisor  # Add the divisor to the operation count
            n //= divisor  # Divide n by the current divisor
        divisor += 1  # Move to the next potential divisor

    return operations
