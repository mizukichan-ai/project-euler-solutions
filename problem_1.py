"""
Project Euler Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_of_3_and_5(n):
    """
    Calculate the sum of all multiples of 3 or 5 below n.
    
    Args:
        n: The upper bound (exclusive)
    
    Returns:
        Sum of all multiples of 3 or 5 below n
    """
    sum_3 = 3 * ((n - 1) // 3) * ((n - 1) // 3 + 1) // 2
    sum_5 = 5 * ((n - 1) // 5) * ((n - 1) // 5 + 1) // 2
    sum_15 = 15 * ((n - 1) // 15) * ((n - 1) // 15 + 1) // 2
    
    return sum_3 + sum_5 - sum_15

def sum_multiples_brute_force(n):
    """
    Alternative brute force approach for verification.
    """
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    n = 1000
    result = sum_multiples_of_3_and_5(n)
    print(f"Sum of multiples of 3 or 5 below {n}: {result}")
    
    # Verify with brute force
    brute_force_result = sum_multiples_brute_force(n)
    print(f"Brute force verification: {brute_force_result}")
    print(f"Results match: {result == brute_force_result}")