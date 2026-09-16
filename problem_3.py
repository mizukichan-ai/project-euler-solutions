"""
Project Euler Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(n):
    """
    Find the largest prime factor of a given number n.
    
    Args:
        n: The number to find the largest prime factor of
    
    Returns:
        The largest prime factor of n
    """
    # Handle factor of 2 separately
    if n % 2 == 0:
        largest_factor = 2
        n = n // 2
        while n % 2 == 0:
            n = n // 2
    else:
        largest_factor = 1
    
    # Check odd factors up to sqrt(n)
    f = 3
    max_factor = int(n**0.5) + 1
    
    while f <= max_factor:
        if n % f == 0:
            largest_factor = f
            n = n // f
            max_factor = int(n**0.5) + 1
            while n % f == 0:
                n = n // f
        f += 2
    
    # If n is still greater than 1, it's prime
    if n > 1:
        largest_factor = n
    
    return largest_factor

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    max_divisor = int(n**0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")
    print(f"Verification: {is_prime(result)} (should be True)")