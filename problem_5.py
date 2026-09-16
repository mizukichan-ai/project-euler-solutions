"""
Project Euler Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers using Euclidean algorithm.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Calculate the least common multiple of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Least common multiple of a and b
    """
    return a * b // gcd(a, b)

def smallest_multiple(n):
    """
    Find the smallest positive number that is evenly divisible by all numbers from 1 to n.
    
    Args:
        n: Upper bound (inclusive)
    
    Returns:
        Smallest number divisible by all numbers from 1 to n
    """
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

def smallest_multiple_prime_factorization(n):
    """
    Alternative approach using prime factorization.
    For each number from 1 to n, find the highest power of each prime that divides it.
    """
    # Sieve of Eratosthenes to find primes up to n
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # For each prime, find the highest power <= n
    result = 1
    for p in primes:
        power = p
        while power * p <= n:
            power *= p
        result *= power
    
    return result

if __name__ == "__main__":
    n = 20
    result = smallest_multiple(n)
    print(f"The smallest positive number divisible by all numbers from 1 to {n} is: {result}")
    
    # Verify with prime factorization approach
    prime_result = smallest_multiple_prime_factorization(n)
    print(f"Prime factorization approach result: {prime_result}")
    print(f"Results match: {result == prime_result}")
    
    # Test the divisibility
    print(f"\nTesting divisibility for numbers 1 to {n}:")
    all_divisible = True
    for i in range(1, n + 1):
        if result % i != 0:
            all_divisible = False
            print(f"❌ {result} % {i} = {result % i}")
    
    if all_divisible:
        print("✅ All divisions successful!")
    else:
        print("❌ Some divisions failed!")